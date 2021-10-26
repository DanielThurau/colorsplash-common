from colorsplash_common import __version__
from colorsplash_common.image_ids import ImageIdsTableHelper
from colorsplash_common.rgb import RGBTableHelper


def test_version():
    assert __version__ == '0.3.0'

def test_ImageIds_attribute_keys():
    imageIds = ImageIdsTableHelper()
    assert imageIds.table_name == "ColorSplashImageIds"
    assert imageIds.image_id_attribute_key == "ImageId"
    assert imageIds.full_url_attribute_key == "FullURL"
    assert imageIds.regular_url_attribute_key == "RegularURL"
    assert imageIds.small_url_attribute_key == "SmallURL"
    assert imageIds.thumbnail_url_attribute_key == "ThumbnailURL"

def test_RGB_attrivute_keys():
    rgb = RGBTableHelper()
    assert rgb.table_name == "ColorSplashRGB"
    assert rgb.rgb_attribute_key == "RGB"
    assert rgb.imageids_attribute_key == "ImageIds"
    assert rgb.all_keys == "RGB, ImageIds"
