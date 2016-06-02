# coding: UTF-8

"""Miral Server API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""


import endpoints
from protorpc import remote

#アカウント関係
from common.msg.AccountServiceMsg import AccountGetMsg
from common.msg.AccountServiceMsg import AccountGetResMsg
from common.msg.AccountServiceMsg import AccountGetLoginMsg
from common.msg.AccountServiceMsg import AccountGetLoginResMsg

from common.service.AccountService import AccountService

#美容師関係
from beauti.service.BeauticianService import BeauticianService

from beauti.msg.BeauticianServiceMsg import BeautiTempAccountAddMsg
from beauti.msg.BeauticianServiceMsg import BeautiTempAccountAddResMsg
from beauti.msg.BeauticianServiceMsg import BeautiTempAccountAddResMsg
from beauti.msg.BeauticianServiceMsg import BeauticianAccountEditMsg
from beauti.msg.BeauticianServiceMsg import BeauticianGetAccountMsg
from beauti.msg.BeauticianServiceMsg import BeauticianGetAccount4EditResMsg

from beauti.msg.BeauticianServiceMsg import  BeautiAccountAddMsg
from beauti.msg.BeauticianServiceMsg import  BeautiAccountAddResMsg
from beauti.msg.BeauticianServiceMsg import  BeauticianModityAccountMsg
from beauti.msg.BeauticianServiceMsg import  BeauticianModityAccountResMsg


#美容師免許関連
from beauti.service.LicenseService import LicenseService

from beauti.msg.LicenseServiceMsg import LicenseAddMsg
from beauti.msg.LicenseServiceMsg import LicenseAddResMsg
from beauti.msg.LicenseServiceMsg import LicenseGetThumbnailImgMsg
from beauti.msg.LicenseServiceMsg  import LicenseGetThumbnailImgResMsg

#サロン関係
from salon.service.SalonService import SalonService
from salon.msg.SalonServiceMsg import SalonAccountAddMsg
from salon.msg.SalonServiceMsg import SalonAccountAddResMsg
from salon.msg.SalonServiceMsg import SalonAccountModifyMsg
from salon.msg.SalonServiceMsg import SalonAccountModifyResMsg
from salon.msg.SalonServiceMsg import SalonGetAccount4EditMsg
from salon.msg.SalonServiceMsg import SalonGetAccount4EditResMsg


#サロンクエリー関係
from salon.service.SalonQueryService import SalonQueryService
from salon.msg.SalonQueryServiceMsg import SalonSearchByKeywordMsg
from salon.msg.SalonQueryServiceMsg import SalonSearchByKeywordResMsg

#サロンギャラリー関係
from salon.service.SalonGalleryService import SalonGalleryService
from salon.msg.SalonGalleryServiceMsg import SalonGalleryAddImgMsg
from salon.msg.SalonGalleryServiceMsg import SalonGalleryAddImgResMsg


#イメージ共通処理関係
from common.service.ImageService  import ImageService
from common.service.ImageService import ImageGetMsg
from common.service.ImageService import ImageGetResMsg 

#マスタ関係
from common.service.TrainMastrService import TrainRouteService
from common.msg.TrainMasterMsg import TrainMasterGetTrainListResMsg 
from common.msg.TrainMasterMsg import TrainMasterGetTrainListMsg 
from common.msg.TrainMasterMsg import TrainMasterSrhStationListResMsg 
from common.msg.TrainMasterMsg import TrainMasterSrhStationListMsg 

from common.MiralLogger import MiralLogger


WEB_CLIENT_ID = '1056231959402-bnjsop84r77gdtlrbb68busanr7d2bla.apps.googleusercontent.com'
ANDROID_AUDIENCE = WEB_CLIENT_ID

package='Mirall'


@endpoints.api(name='miralServer', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID,endpoints.API_EXPLORER_CLIENT_ID],
               audiences=[ANDROID_AUDIENCE],
               scopes=[endpoints.EMAIL_SCOPE])
class MiralServerApi(remote.Service):
    """MiralServer AIP v1"""

    ########################################
    #アカウント関係
    @endpoints.method(AccountGetMsg, AccountGetResMsg,
                     path='coomon/accountservice/get', http_method='POST',
                     name='common.accountservice.get')

    def common_accountservice_get(self, request): 
        u"""アカウント情報の取得"""
        
        logger = MiralLogger()
        
        logger.debug(u"★"+"loginType:"+str(request.loginType)+ " id:"+request.id)
        
        service = AccountService();
        return service.get(request.loginType, request.id)

    #ログイン
    @endpoints.method(AccountGetLoginMsg, AccountGetLoginResMsg,
                     path='coomon/accountservice/getlogin', http_method='POST',
                     name='common.accountservice.getlogin')

    def common_accountservice_getlogin(self, request): 
        u"""アカウント情報の取得"""
        
        logger = MiralLogger()
        
        logger.debug(u"★"+"loginType:"+str(request.loginType)+ " id:"+request.id)
        
        service = AccountService();
        return service.getLogin(request.loginType, request.id)


    ########################################
    #美容師関係

    #美容師仮登録
    @endpoints.method(BeautiTempAccountAddMsg, BeautiTempAccountAddResMsg,
                     path='beauti/beauticianservice/addtemp', http_method='POST',
                     name='beauti.beauticianservice.addtemp')

    def beauti_beauticianservice_addtemp(self, request): 
        u"""美容師アカウント情報の仮登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_beauticianservice_addtemp")
        
        service = BeauticianService();
        return service.addTempAccount(request)

    #アカウント設定画面情報取得
    @endpoints.method(BeauticianGetAccountMsg, BeauticianGetAccount4EditResMsg,
                     path='beauti/beauticianservice/getacc4edit', http_method='POST',
                     name='beauti.beauticianservice.getacc4edit')

    def beauti_beauticianservice_getacc4edit(self, request): 
        u"""美容師アカウント情報の仮登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_beauticianservice_getacc4edit:"+request.accountId)
        
        service = BeauticianService();
        return service.getAccount4Edit(request)
    
    #アカウント新規登録
    @endpoints.method(BeautiAccountAddMsg, BeautiAccountAddResMsg,
                     path='beauti/beauticianservice/add', http_method='POST',
                     name='beauti.beauticianservice.add')

    def beauti_beauticianservice_add(self, request): 
        u"""美容師アカウント情報の登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_beauticianservice_add")
        
        service = BeauticianService();
        return service.add(request)
    
    #アカウント情報変更
    @endpoints.method(BeauticianModityAccountMsg, BeauticianModityAccountResMsg,
                     path='beauti/beauticianservice/modify', http_method='POST',
                     name='beauti.beauticianservice.modify')

    def beauti_beauticianservice_modify(self, request): 
        u"""美容師アカウント情報の変更"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_beauticianservice_modify:"+request.accountId)
        
        service = BeauticianService()
        return service.modify(request)
    
    
    
    #美容師免許の登録
    @endpoints.method(LicenseAddMsg, LicenseAddResMsg,
                     path='beauti/licenseservice/set', http_method='POST',
                     name='beauti.licenseservice.set')

    def beauti_licenseservice_set(self, request): 
        u"""美容師の美容師免許の新規登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_licenseimgservice_set")
        logger.debug("beautiId:"+str(request.beautiId))
        
        service = LicenseService();
        return service.set(request.beautiId, request.imgbase64data)

    #美容師免許サムネイル画像の取得
    @endpoints.method(LicenseGetThumbnailImgMsg, LicenseGetThumbnailImgResMsg,
                     path='beauti/licenseservice/getthumbnailimage', http_method='POST',
                     name='beauti.licenseservice.getthumbnailimage')

    def beauti_licenseservice_getthumbnailimage(self, request): 
        u"""美容師の美容師免許の新規登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_licenseservice_getthumbnailimage")
        logger.debug("beautiId:"+str(request.beautiId))
        
        service = LicenseService();
        return service.getThumbnailImage(request.beautiId)

    ########################################
    #サロンクエリー関連
    
    #サロン検索
    @endpoints.method(SalonSearchByKeywordMsg, SalonSearchByKeywordResMsg,
                     path='salon/salonqueryservice/srhbykeyword', http_method='POST',
                     name='salon.salonqueryservice.srhbykeyword')

    def salon_salonqueryservice_srhbykeyword(self, request): 
        u"""サロンアカウント情報の登録"""
        
        logger = MiralLogger()
        
        logger.debug(u"★salon_salonqueryservice_srhbykeyword")
        
        service = SalonQueryService()
        return service.searchByKeyword(request)

    
    ########################################
    #サロン関連
    
    #アカウント新規登録
    @endpoints.method(SalonAccountAddMsg, SalonAccountAddResMsg,
                     path='salon/salonservice/add', http_method='POST',
                     name='salon.salonservice.add')

    def salon_salonservice_add(self, request): 
        u"""サロンアカウント情報の登録"""
        
        logger = MiralLogger()
        
        logger.debug(u"★salon_salonservice_add")
        
        service = SalonService()
        return service.add(request)

    #アカウント修正
    @endpoints.method(SalonAccountModifyMsg, SalonAccountModifyResMsg,
                     path='salon/salonservice/modify', http_method='POST',
                     name='salon.salonservice.modify')

    def salon_salonservice_modify(self, request): 
        u"""サロンアカウント情報の登録"""
        
        logger = MiralLogger()
        
        logger.debug(u"★salon_salonservice_add")
        
        service = SalonService()
        return service.modify(request)

    #アカウント情報取得
    @endpoints.method(SalonGetAccount4EditMsg, SalonGetAccount4EditResMsg,
                     path='salon/salonservice/getaccount4edit', http_method='POST',
                     name='salon.salonservice.getaccount4edit')

    def salon_salonservice_getaccount4edit(self, request): 
        u"""サロンアカウント情報の登録"""
        
        logger = MiralLogger()
        
        logger.debug(u"★salon_salonservice_getaccount4edit")
        
        service = SalonService()
        return service.getAccount4Edit(request)

    ########################################
    #サロン ギャラリ関連
    
    #画像追加登録
    @endpoints.method(SalonGalleryAddImgMsg, SalonGalleryAddImgResMsg,
                     path='salon/salongalleryservice/add', http_method='POST',
                     name='salon.salongalleryservice.add')

    def salon_salongalleryservice_add(self, request): 
        u"""サロンギャラリ画像追加登録"""
        
        logger = MiralLogger()
        
        logger.debug(u"★salon_salongalleryservice_add")
        
        service = SalonGalleryService()
        return service.add(request.salonId, request.imgbase64data)


    
    ########################################
    #マスタ関係
    @endpoints.method(TrainMasterGetTrainListMsg, TrainMasterGetTrainListResMsg,
                     path='common/trainmasterservice/gettrainlist', http_method='POST',
                     name='common.trainmasterservice.gettrainlist')

    #マスタ関係
    def common_trainmasterservice_gettrainlist(self, request): 
        u"""沿線リスト取得"""
        logger = MiralLogger()
        
        logger.debug(u"★common_trainmasterservice_gettrainlist")
        
        service = TrainRouteService()
        return service.getTrainList(request)
    
    @endpoints.method(TrainMasterSrhStationListMsg, TrainMasterSrhStationListResMsg,
                     path='common/trainmasterservice/srhstationlist', http_method='POST',
                     name='common.trainmasterservice.srhstationlist')

    def common_trainmasterservice_srhstationlist(self, request): 
        u"""駅リスト取得"""
        logger = MiralLogger()
        
        logger.debug(u"★common_trainmasterservice_srhstationlist")
        
        service = TrainRouteService()
        return service.srhStationList(request.keyword)
    
    
    ###################################################################
    ###################################################################
    ###################################################################
    ###################################################################
    
    
    

    ########################################
    #イメージ共通処理関係
    @endpoints.method(ImageGetMsg, ImageGetResMsg,
                     path='common/imageservice/load', http_method='POST',
                     name='common.imageservice.load')

    def beauti_imageservice_load(self, request): 
        u"""画像データの読み込み"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_imgservice_load")
        logger.debug("fileName:"+str(request.fileName))
        
        service = ImageService();
        return service.load(request.fileName)
    

    """//////////////////////////////////////////////////////
    
    """
    





        
APPLICATION = endpoints.api_server([MiralServerApi])

            
        
    
    
    


