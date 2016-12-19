# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.achievement_definition_resource import AchievementDefinitionResource
from .models.achievement_progress_update_request import AchievementProgressUpdateRequest
from .models.action_resource import ActionResource
from .models.action_variable_resource import ActionVariableResource
from .models.activity_entitlement_resource import ActivityEntitlementResource
from .models.activity_occurrence_creation_failure import ActivityOccurrenceCreationFailure
from .models.activity_occurrence_join_result import ActivityOccurrenceJoinResult
from .models.activity_occurrence_resource import ActivityOccurrenceResource
from .models.activity_occurrence_results import ActivityOccurrenceResults
from .models.activity_resource import ActivityResource
from .models.activity_user_resource import ActivityUserResource
from .models.address_resource import AddressResource
from .models.affiliate import Affiliate
from .models.aggregate_count_resource import AggregateCountResource
from .models.aggregate_invoice_report_resource import AggregateInvoiceReportResource
from .models.amazon_s3_activity import AmazonS3Activity
from .models.answer_resource import AnswerResource
from .models.apply_payment_request import ApplyPaymentRequest
from .models.article_resource import ArticleResource
from .models.artist import Artist
from .models.artist_resource import ArtistResource
from .models.available_setting_resource import AvailableSettingResource
from .models.bare_activity_resource import BareActivityResource
from .models.bare_challenge_activity_resource import BareChallengeActivityResource
from .models.batch import Batch
from .models.batch_request import BatchRequest
from .models.batch_return import BatchReturn
from .models.behavior import Behavior
from .models.billing_report import BillingReport
from .models.boolean_resource import BooleanResource
from .models.bre_category_resource import BreCategoryResource
from .models.bre_event import BreEvent
from .models.bre_event_log import BreEventLog
from .models.bre_global_resource import BreGlobalResource
from .models.bre_global_scope_definition import BreGlobalScopeDefinition
from .models.bre_rule import BreRule
from .models.bre_rule_log import BreRuleLog
from .models.bre_trigger_parameter_definition import BreTriggerParameterDefinition
from .models.bre_trigger_resource import BreTriggerResource
from .models.bundle_item import BundleItem
from .models.bundled_sku import BundledSku
from .models.campaign_resource import CampaignResource
from .models.cart import Cart
from .models.cart_item_request import CartItemRequest
from .models.cart_line_item import CartLineItem
from .models.cart_shippable_response import CartShippableResponse
from .models.cart_shipping_address_request import CartShippingAddressRequest
from .models.cart_shipping_option import CartShippingOption
from .models.cart_summary import CartSummary
from .models.catalog_sale import CatalogSale
from .models.category_resource import CategoryResource
from .models.challenge_activity_resource import ChallengeActivityResource
from .models.challenge_event_participant_resource import ChallengeEventParticipantResource
from .models.challenge_event_resource import ChallengeEventResource
from .models.challenge_resource import ChallengeResource
from .models.city_resource import CityResource
from .models.client_resource import ClientResource
from .models.collection_country import CollectionCountry
from .models.collection_video_contribution import CollectionVideoContribution
from .models.collectionstring import Collectionstring
from .models.comment_resource import CommentResource
from .models.comment_search import CommentSearch
from .models.config import Config
from .models.contribution_resource import ContributionResource
from .models.country import Country
from .models.country_resource import CountryResource
from .models.country_tax_resource import CountryTaxResource
from .models.coupon_definition import CouponDefinition
from .models.coupon_item import CouponItem
from .models.create_billing_agreement_request import CreateBillingAgreementRequest
from .models.create_pay_pal_payment_request import CreatePayPalPaymentRequest
from .models.currency import Currency
from .models.currency_resource import CurrencyResource
from .models.customer_config import CustomerConfig
from .models.customer_resource import CustomerResource
from .models.database_config import DatabaseConfig
from .models.delta_resource import DeltaResource
from .models.device_resource import DeviceResource
from .models.discount import Discount
from .models.disposition_count import DispositionCount
from .models.disposition_resource import DispositionResource
from .models.entitlement_item import EntitlementItem
from .models.expressionobject import Expressionobject
from .models.finalize_billing_agreement_request import FinalizeBillingAgreementRequest
from .models.finalize_pay_pal_payment_request import FinalizePayPalPaymentRequest
from .models.flag_report_resource import FlagReportResource
from .models.flag_resource import FlagResource
from .models.forward_log import ForwardLog
from .models.fulfillment_type import FulfillmentType
from .models.google_payment_request import GooglePaymentRequest
from .models.grant_type_resource import GrantTypeResource
from .models.group import Group
from .models.group_member import GroupMember
from .models.group_member_resource import GroupMemberResource
from .models.group_resource import GroupResource
from .models.import_job_output_resource import ImportJobOutputResource
from .models.import_job_resource import ImportJobResource
from .models.inventory_subscription_resource import InventorySubscriptionResource
from .models.invoice_create_request import InvoiceCreateRequest
from .models.invoice_item_resource import InvoiceItemResource
from .models.invoice_log_entry import InvoiceLogEntry
from .models.invoice_payment_status_request import InvoicePaymentStatusRequest
from .models.invoice_resource import InvoiceResource
from .models.item_behavior_definition_resource import ItemBehaviorDefinitionResource
from .models.item_template_resource import ItemTemplateResource
from .models.key_value_pairstringstring import KeyValuePairstringstring
from .models.language import Language
from .models.leaderboard_entry_resource import LeaderboardEntryResource
from .models.leaderboard_resource import LeaderboardResource
from .models.leveling_resource import LevelingResource
from .models.localizer import Localizer
from .models.location_log_resource import LocationLogResource
from .models.lookup_type_resource import LookupTypeResource
from .models.maintenance import Maintenance
from .models.mapstringobject import Mapstringobject
from .models.metric_resource import MetricResource
from .models.model_property import ModelProperty
from .models.mongo_database_config import MongoDatabaseConfig
from .models.nested_category import NestedCategory
from .models.new_password_request import NewPasswordRequest
from .models.oauth_access_token_resource import OauthAccessTokenResource
from .models.operator import Operator
from .models.optimal_payment_request import OptimalPaymentRequest
from .models.page_achievement_definition_resource import PageAchievementDefinitionResource
from .models.page_aggregate_count_resource import PageAggregateCountResource
from .models.page_aggregate_invoice_report_resource import PageAggregateInvoiceReportResource
from .models.page_article_resource import PageArticleResource
from .models.page_artist_resource import PageArtistResource
from .models.page_bare_activity_resource import PageBareActivityResource
from .models.page_bare_challenge_activity_resource import PageBareChallengeActivityResource
from .models.page_billing_report import PageBillingReport
from .models.page_bre_category_resource import PageBreCategoryResource
from .models.page_bre_event_log import PageBreEventLog
from .models.page_bre_global_resource import PageBreGlobalResource
from .models.page_bre_rule import PageBreRule
from .models.page_bre_trigger_resource import PageBreTriggerResource
from .models.page_campaign_resource import PageCampaignResource
from .models.page_cart_summary import PageCartSummary
from .models.page_catalog_sale import PageCatalogSale
from .models.page_category_resource import PageCategoryResource
from .models.page_challenge_event_participant_resource import PageChallengeEventParticipantResource
from .models.page_challenge_event_resource import PageChallengeEventResource
from .models.page_challenge_resource import PageChallengeResource
from .models.page_client_resource import PageClientResource
from .models.page_comment_resource import PageCommentResource
from .models.page_config import PageConfig
from .models.page_country_tax_resource import PageCountryTaxResource
from .models.page_currency_resource import PageCurrencyResource
from .models.page_device_resource import PageDeviceResource
from .models.page_disposition_resource import PageDispositionResource
from .models.page_entitlement_item import PageEntitlementItem
from .models.page_flag_report_resource import PageFlagReportResource
from .models.page_forward_log import PageForwardLog
from .models.page_fulfillment_type import PageFulfillmentType
from .models.page_group_member_resource import PageGroupMemberResource
from .models.page_group_resource import PageGroupResource
from .models.page_import_job_resource import PageImportJobResource
from .models.page_invoice_log_entry import PageInvoiceLogEntry
from .models.page_invoice_resource import PageInvoiceResource
from .models.page_item_template_resource import PageItemTemplateResource
from .models.page_leveling_resource import PageLevelingResource
from .models.page_location_log_resource import PageLocationLogResource
from .models.page_mapstringobject import PageMapstringobject
from .models.page_oauth_access_token_resource import PageOauthAccessTokenResource
from .models.page_permission_resource import PagePermissionResource
from .models.page_poll_resource import PagePollResource
from .models.page_question_resource import PageQuestionResource
from .models.page_question_template_resource import PageQuestionTemplateResource
from .models.page_revenue_country_report_resource import PageRevenueCountryReportResource
from .models.page_revenue_product_report_resource import PageRevenueProductReportResource
from .models.page_reward_set_resource import PageRewardSetResource
from .models.page_role_resource import PageRoleResource
from .models.page_saved_address_resource import PageSavedAddressResource
from .models.page_simple_user_resource import PageSimpleUserResource
from .models.page_simple_wallet import PageSimpleWallet
from .models.page_state_tax_resource import PageStateTaxResource
from .models.page_store_item import PageStoreItem
from .models.page_store_item_template_resource import PageStoreItemTemplateResource
from .models.page_subscription_resource import PageSubscriptionResource
from .models.page_subscription_template_resource import PageSubscriptionTemplateResource
from .models.page_template_resource import PageTemplateResource
from .models.page_transaction_resource import PageTransactionResource
from .models.page_usage_info import PageUsageInfo
from .models.page_user_achievement_group_resource import PageUserAchievementGroupResource
from .models.page_user_action_log import PageUserActionLog
from .models.page_user_base_resource import PageUserBaseResource
from .models.page_user_inventory_resource import PageUserInventoryResource
from .models.page_user_item_log_resource import PageUserItemLogResource
from .models.page_user_leveling_resource import PageUserLevelingResource
from .models.page_user_relationship_resource import PageUserRelationshipResource
from .models.page_vendor_resource import PageVendorResource
from .models.page_video_relationship_resource import PageVideoRelationshipResource
from .models.page_video_resource import PageVideoResource
from .models.page_wallet_total_response import PageWalletTotalResponse
from .models.page_wallet_transaction_resource import PageWalletTransactionResource
from .models.pagestring import Pagestring
from .models.pay_by_saved_method_request import PayBySavedMethodRequest
from .models.payment_authorization_resource import PaymentAuthorizationResource
from .models.payment_method_resource import PaymentMethodResource
from .models.payment_method_type_resource import PaymentMethodTypeResource
from .models.permission import Permission
from .models.permission_resource import PermissionResource
from .models.poll_answer_resource import PollAnswerResource
from .models.poll_resource import PollResource
from .models.poll_response_resource import PollResponseResource
from .models.predicate_operation import PredicateOperation
from .models.property_definition_resource import PropertyDefinitionResource
from .models.question_resource import QuestionResource
from .models.question_template_resource import QuestionTemplateResource
from .models.raw_email_resource import RawEmailResource
from .models.raw_sms_resource import RawSMSResource
from .models.reactivate_subscription_request import ReactivateSubscriptionRequest
from .models.refund_request import RefundRequest
from .models.refund_resource import RefundResource
from .models.result import Result
from .models.revenue_country_report_resource import RevenueCountryReportResource
from .models.revenue_product_report_resource import RevenueProductReportResource
from .models.revenue_report_resource import RevenueReportResource
from .models.reward_currency_resource import RewardCurrencyResource
from .models.reward_item_resource import RewardItemResource
from .models.reward_set_resource import RewardSetResource
from .models.role import Role
from .models.role_resource import RoleResource
from .models.sample_countries_response import SampleCountriesResponse
from .models.saved_address_resource import SavedAddressResource
from .models.schedule import Schedule
from .models.search_reference_mapping import SearchReferenceMapping
from .models.selected_setting_resource import SelectedSettingResource
from .models.setting_option import SettingOption
from .models.shipping_item import ShippingItem
from .models.simple_reference_resourceint import SimpleReferenceResourceint
from .models.simple_reference_resourcelong import SimpleReferenceResourcelong
from .models.simple_reference_resourcestring import SimpleReferenceResourcestring
from .models.simple_user_resource import SimpleUserResource
from .models.simple_wallet import SimpleWallet
from .models.sku import Sku
from .models.sku_request import SkuRequest
from .models.sort import Sort
from .models.sql_database_config import SqlDatabaseConfig
from .models.state_resource import StateResource
from .models.state_tax_resource import StateTaxResource
from .models.store_item import StoreItem
from .models.store_item_template_resource import StoreItemTemplateResource
from .models.store_list_request import StoreListRequest
from .models.stripe_create_payment_method import StripeCreatePaymentMethod
from .models.stripe_payment_request import StripePaymentRequest
from .models.subscription_credit_resource import SubscriptionCreditResource
from .models.subscription_plan_resource import SubscriptionPlanResource
from .models.subscription_resource import SubscriptionResource
from .models.subscription_template_resource import SubscriptionTemplateResource
from .models.template_email_resource import TemplateEmailResource
from .models.template_resource import TemplateResource
from .models.template_sms_resource import TemplateSMSResource
from .models.tier_resource import TierResource
from .models.timezone import Timezone
from .models.token_details_resource import TokenDetailsResource
from .models.transaction_resource import TransactionResource
from .models.usage_info import UsageInfo
from .models.user import User
from .models.user_achievement_group_resource import UserAchievementGroupResource
from .models.user_achievement_resource import UserAchievementResource
from .models.user_action_log import UserActionLog
from .models.user_activity_results_resource import UserActivityResultsResource
from .models.user_base_resource import UserBaseResource
from .models.user_inventory_add_request import UserInventoryAddRequest
from .models.user_inventory_resource import UserInventoryResource
from .models.user_item_log_resource import UserItemLogResource
from .models.user_leveling_resource import UserLevelingResource
from .models.user_relationship import UserRelationship
from .models.user_relationship_reference_resource import UserRelationshipReferenceResource
from .models.user_relationship_resource import UserRelationshipResource
from .models.user_resource import UserResource
from .models.user_tag import UserTag
from .models.variable_type_resource import VariableTypeResource
from .models.vendor_resource import VendorResource
from .models.video import Video
from .models.video_contribution import VideoContribution
from .models.video_relationship_resource import VideoRelationshipResource
from .models.video_resource import VideoResource
from .models.video_tag import VideoTag
from .models.wallet_alter_request import WalletAlterRequest
from .models.wallet_total_response import WalletTotalResponse
from .models.wallet_transaction_resource import WalletTransactionResource
from .models.xsolla_payment_request import XsollaPaymentRequest

# import apis into sdk package
from .apis.awss3_api import AWSS3Api
from .apis.activities_api import ActivitiesApi
from .apis.auth_clients_api import AuthClientsApi
from .apis.auth_permissions_api import AuthPermissionsApi
from .apis.auth_roles_api import AuthRolesApi
from .apis.auth_tokens_api import AuthTokensApi
from .apis.bre_rule_engine_actions_api import BRERuleEngineActionsApi
from .apis.bre_rule_engine_categories_api import BRERuleEngineCategoriesApi
from .apis.bre_rule_engine_events_api import BRERuleEngineEventsApi
from .apis.bre_rule_engine_expressions_api import BRERuleEngineExpressionsApi
from .apis.bre_rule_engine_globals_api import BRERuleEngineGlobalsApi
from .apis.bre_rule_engine_rules_api import BRERuleEngineRulesApi
from .apis.bre_rule_engine_triggers_api import BRERuleEngineTriggersApi
from .apis.bre_rule_engine_variables_api import BRERuleEngineVariablesApi
from .apis.campaigns_api import CampaignsApi
from .apis.campaigns_challenges_api import CampaignsChallengesApi
from .apis.campaigns_rewards_api import CampaignsRewardsApi
from .apis.categories_api import CategoriesApi
from .apis.configs_api import ConfigsApi
from .apis.content_articles_api import ContentArticlesApi
from .apis.content_comments_api import ContentCommentsApi
from .apis.content_polls_api import ContentPollsApi
from .apis.currencies_api import CurrenciesApi
from .apis.customerservice_api import CustomerserviceApi
from .apis.devices_api import DevicesApi
from .apis.dispositions_api import DispositionsApi
from .apis.fulfillment_api import FulfillmentApi
from .apis.gamification_achievements_api import GamificationAchievementsApi
from .apis.gamification_leaderboards_api import GamificationLeaderboardsApi
from .apis.gamification_leveling_api import GamificationLevelingApi
from .apis.gamification_metrics_api import GamificationMetricsApi
from .apis.gamification_trivia_api import GamificationTriviaApi
from .apis.invoices_api import InvoicesApi
from .apis.locations_api import LocationsApi
from .apis.logs_api import LogsApi
from .apis.media_artists_api import MediaArtistsApi
from .apis.media_moderation_api import MediaModerationApi
from .apis.media_videos_api import MediaVideosApi
from .apis.messaging_api import MessagingApi
from .apis.payments_api import PaymentsApi
from .apis.payments_apple_api import PaymentsAppleApi
from .apis.payments_google_api import PaymentsGoogleApi
from .apis.payments_optimal_api import PaymentsOptimalApi
from .apis.payments_pay_pal_classic_api import PaymentsPayPalClassicApi
from .apis.payments_stripe_api import PaymentsStripeApi
from .apis.payments_transactions_api import PaymentsTransactionsApi
from .apis.payments_wallets_api import PaymentsWalletsApi
from .apis.payments_xsolla_api import PaymentsXsollaApi
from .apis.reporting_challenges_api import ReportingChallengesApi
from .apis.reporting_orders_api import ReportingOrdersApi
from .apis.reporting_revenue_api import ReportingRevenueApi
from .apis.reporting_subscriptions_api import ReportingSubscriptionsApi
from .apis.reporting_usage_api import ReportingUsageApi
from .apis.reporting_users_api import ReportingUsersApi
from .apis.search_api import SearchApi
from .apis.store_api import StoreApi
from .apis.store_bundles_api import StoreBundlesApi
from .apis.store_coupons_api import StoreCouponsApi
from .apis.store_sales_api import StoreSalesApi
from .apis.store_shipping_api import StoreShippingApi
from .apis.store_shopping_carts_api import StoreShoppingCartsApi
from .apis.store_subscriptions_api import StoreSubscriptionsApi
from .apis.store_vendors_api import StoreVendorsApi
from .apis.taxes_api import TaxesApi
from .apis.users_api import UsersApi
from .apis.users_addresses_api import UsersAddressesApi
from .apis.users_friendships_api import UsersFriendshipsApi
from .apis.users_groups_api import UsersGroupsApi
from .apis.users_inventory_api import UsersInventoryApi
from .apis.users_relationships_api import UsersRelationshipsApi
from .apis.users_subscriptions_api import UsersSubscriptionsApi
from .apis.util_batch_api import UtilBatchApi
from .apis.util_health_api import UtilHealthApi
from .apis.util_maintenance_api import UtilMaintenanceApi
from .apis.util_security_api import UtilSecurityApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
