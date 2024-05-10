from PIL import Image, ExifTags

# Open the image file
with Image.open("image.jpg") as img:

    # Get any available EXIF metadata
    exif_data = img.getexif()
    if exif_data:
        # Get the ID for the GPSInfo tag
        gps_info = exif_data.get(34853)
        if gps_info:
            # Extract the GPS coordinates from the GPSInfo tag
            lat_ref = gps_info[1]
            lat_deg = gps_info[2][0][0] / gps_info[2][0][1]
            lat_min = gps_info[2][1][0] / gps_info[2][1][1]
            lat_sec = gps_info[2][2][0] / gps_info[2][2][1]
            lat = lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0)
            if lat_ref == "S":
                lat = -lat

            lon_ref = gps_info[3]
            lon_deg = gps_info[4][0][0] / gps_info[4][0][1]
            lon_min = gps_info[4][1][0] / gps_info[4][1][1]
            lon_sec = gps_info[4][2][0] / gps_info[4][2][1]
            lon = lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0)
            if lon_ref == "W":
                lon = -lon

            print(f"GPS coordinates: ({lat}, {lon})")
        else:
            print("No GPS information found.")
    else:
        print("No EXIF metadata found.")
