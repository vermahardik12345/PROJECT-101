import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.A4o_VI_JzHx9dDCVKCCHoVR6VO-59mEVsT2Gh9p2K7k7CIUJRF8cWVAe5D5SSF8Ve9ILmnuV88fwuX4i5vEfYa5GcrC4aPJokcvG18BaIzbhXgUlOJ_v3_6M2EB_j_HqMKWVbRlr_4Zu'
    transferData=TransferData(access_token)
    file_from=input('Write the path of the file which you want to upload')
    file_to=input('Enter the full path to uplaod')
    print('Uploaded Successfully')
    transferData.upload_file(file_from,file_to)  
if __name__=='__main__':
    main()    

