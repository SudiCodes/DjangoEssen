# DjangoEssen
This is a Django application with most of the commonly used usecases


# GOAL
This branch is dedicated to create a backend which can handle file upload with below feats:
 - Large file uploads(Upto 4GB)
 - Resumable Downloads
 - Multiple files
 - safe and secure 


# NOTES
A view handling this form will receive the file data in request.FILES, which is a dictionary containing a key for each FileField (or ImageField, or other FileField subclass) in the form. So the data from the above form would be accessible as request.FILES['file'].

Note that request.FILES will only contain data if the request method was POST, at least one file field was actually posted, and the <form> that posted the request has the attribute enctype="multipart/form-data"

By default, if an uploaded file is smaller than 2.5 megabytes, Django will hold the entire contents of the upload in memory. This means that saving the file involves only a read from memory and a write to disk and thus is very fast.

if an uploaded file is too large, Django will write the uploaded file to a temporary file stored in your system’s temporary directory. On a Unix-like platform this means you can expect Django to generate a file called something like /tmp/tmpzfp6I6.upload. If an upload is large enough, you can watch this file grow in size as Django streams the data onto disk


# File Upload settings variables
FILE_UPLOAD_HANDLERS

FILE_UPLOAD_MAX_MEMORY_SIZE

FILE_UPLOAD_PERMISSIONS

FILE_UPLOAD_TEMP_DIR

MEDIA_ROOT

MEDIA_URL

STORAGES