"""
list_raster: List[DatasetReader] = []
for idx in get_path_idx(path_lc)[:2]:
    raster_idx: DatasetReader = rasterio.open(path_tile)
    list_raster.append(raster_idx)
    break


mosaic, out_trans = merge(list_raster)
print(type(mosaic.dtype))

with rasterio.open(path_out, 'w', driver = 'GTiff',
        height = mosaic.shape[1],
        width = mosaic.shape[2],
        count = mosaic.shape[0],
        dtype = str(mosaic.dtype),
        crs = raster_idx.crs,
        transform = out_trans,
        compress = 'lzw') as dest:
    dest.write(mosaic)
"""