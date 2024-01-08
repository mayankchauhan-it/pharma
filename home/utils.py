# utils.py
def get_upload_path(instance, filename):
    # 'pictures/hospital_id/images/filename'
    return f'pictures/{instance.hmid.id}/images/{filename}'
