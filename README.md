# Dropbox Uploader

Super Simple Dropbox Uploader

## Usage

You would need a dropbox access token to upload your files.
+ You need to create an Dropbox Application to make API requests at https://dropbox.com/developers/apps.
+ Once you've created an app, you can go to the app's console and generate an access token for your own Dropbox account.


```
docker run -v $PWD:/mount jtmiclat/dropbox-uploader --token <dropbox_uploader>> --source <file_to_upload> --target <path_in_dropbox>
```