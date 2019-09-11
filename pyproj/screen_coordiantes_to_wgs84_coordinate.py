import shapely
import pyproj

from functools import partial
from shapely.ops import transform
from shapely.geometry import point as shapelypoint
from shapely.geometry import box as shapelybox

# Setup wgs84 (= EPSG 4326) projection
p_wgs84_4326 = pyproj.Proj("+init=EPSG:4326")

# Setup wgs84 (= EPSG 3857) projection
p_wgs84_3857 = pyproj.Proj("+init=EPSG:3857")


# Setup transformation EPSG 4326 to EPSG 3857
project_meters = partial(
    pyproj.transform,
    p_wgs84_4326,
    p_wgs84_3857
)

# Setup transformation EPSG 3857 to EPSG 4326
project_degrees = partial(
    pyproj.transform,
    p_wgs84_3857,
    p_wgs84_4326
)

TILE_ORIGIN = "top_left"

TILE_SIZE, SCALES = (
    512, [
        78271.51695,  # 0
        39135.758475,
        19567.8792375,
        9783.93961875,
        4891.969809375,
        2445.9849046875,
        1222.99245234375,
        611.496226171875,
        305.7481130859375,
        152.87405654296876,
        76.43702827148438,
        38.21851413574219,
        19.109257067871095,
        9.554628533935547,
        4.777314266967774,
        2.388657133483887,
        1.1943285667419434,
        0.5971642833709717  # 17
    ]
)

REFERENCE_POINTS = {

    # Google-Mercator
    '+init=epsg:3857': [
        (-180, -85.05112877980659),
        (-180, 85.0511287798066),
        (180, -85.05112877980659),
        (180, 85.0511287798066)
    ],

    'default': [
        (-180, -90),
        (-180, 0),
        (-180, 90),
        (0, 90),
        (180, 90),
        (180, 0),
        (180, -90),
        (0, -90),
    ],
}


def compute_bounds():
    border_points = REFERENCE_POINTS.get('+init=epsg:3857', REFERENCE_POINTS['default'])

    max_x = max_y = float("-infinity")
    min_x = min_y = float("infinity")

    for point in border_points:

        point = shapelypoint.Point(*point)

        # Project the border points following the projection system
        point = shapelypoint.Point(
            p_wgs84_3857(point.x, point.y)
        )

        # Ignore the border points which cannot be projected

        if point.x != float("infinity") or point.y != float("infinity"):
            # Compute the smallest bounds containing the border points
            min_x = min(point.x, min_x)
            max_x = max(point.x, max_x)
            min_y = min(point.y, min_y)
            max_y = max(point.y, max_y)

    return min_x, min_y, max_x, max_y


def get_tile_side(zoom):
    return TILE_SIZE * SCALES[zoom]


def xyz_to_box2d(sx, sy, zoom):
    """ Convert XYZ to mapnik.Box2d """

    _min_x, _min_y, _max_x, _max_y = compute_bounds()

    tile_side = get_tile_side(zoom)

    min_x = sx * tile_side + _min_x

    max_x = min_x + tile_side

    max_y = _max_y - sy * tile_side

    min_y = max_y - tile_side


    return shapelybox(min_x, min_y, max_x, max_y)


def reproj_bbox(bbox):
    """

    This static method performs a reprojection from Marcator to Lat/Lon.

    :param bbox: The bbox to reproject.

    :return: This method returns the bbox reprojected.

    """

    print("Mercator ", bbox)

    # Convert to WGS84
    new_bbox = transform(
        project_degrees,
        bbox
    )

    print("WGS84   ", new_bbox)

    long1, lat1, long2, lat2 = tuple(new_bbox.envelope.bounds)

    return lat1, long1, lat2, long2


if __name__ == '__main__':
    zoom, x, y = 10, 518, 352
    box2d = xyz_to_box2d(zoom=zoom, sx=x, sy=y)
    print("box2d", box2d)
    bbox = reproj_bbox(box2d)
    print("bbox", bbox)