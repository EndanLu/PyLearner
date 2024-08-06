from diagrams import Diagram, Cluster, Node
from diagrams.aws.network import APIGateway, ALB
from diagrams.aws.compute import ECS, Fargate, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.storage import S3
from diagrams.generic.database import SQL
from diagrams.aws.integration import SNS, SQS


with Diagram("AIM Backend AWS Architecture & Data Flow", show=False):
    user = SQL("User Client", image="Res/user.png")  # 使用 Node 类表示用户
    redis = SQL("Redis", image="Res/redis.png")  # 使用 diagrams.aws.cache.Redis 表示 Redis
    vfap = SQL("VFAP", image="Res/data.png")  # 假设 VFAP 是一个自定义服务，没有现成的图标
    rpa = SQL("RPA", image="Res/rpa.png")  # 假设 RPA 是一个自定义服务
    vmid = SQL("VMID", image="Res/oms.png")  # 假设 VMID 是一个自定义
    sap = SQL("SAP", image="Res/sap.png")  # 假设 SAP 是一个自定义服务

    sns = SNS("SNS")
    sqs = SQS("SQS")

    api_gateway = APIGateway("API Gateway")

    lambda_function = Lambda("Lambda")

    with Cluster("Lambda"):
        lambda_in_season = Lambda("In-Season")
        lambda_pre_season = Lambda("Pre-Season")
        lambda_new_products = Lambda("New-Products")

    with Cluster("VPC Private Subnet"):
        ecs = ECS("ECS Service")

        with Cluster("ECS Cluster"):
            fargate1 = Fargate("Fargate(JavaSpring)")
            fargate2 = Fargate("Fargate(JavaSpring)")

        alb = ALB("ALB")

    cloudwatch = Cloudwatch("CloudWatch")

    rds = RDS("RDS")
    s3 = S3("Amazon S3")

    user >> api_gateway >> alb >> ecs >> [fargate1, fargate2]

    ecs >> lambda_function

    lambda_function >> [lambda_in_season, lambda_pre_season, lambda_new_products]
    lambda_function >> rds

    ecs >> [redis, rds]

    cloudwatch >> ecs
    cloudwatch >> lambda_function

    # 添加 SNS 服务来监控 S3 的变化，并连接到 VFAP 和 SQS 服务
    ecs << s3
    ecs >> s3

    s3 >> sns >> [vfap, sqs]
    sqs >> ecs

    # ecs >> rpa >> sap
    # vfap >> s3

    ecs << vmid

    ecs >> rpa >> sap

    rpa >> s3