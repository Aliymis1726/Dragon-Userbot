import environs

env = environs.Env()
env.read_env("./.env")

api_id = env.int("25574009")
api_hash = env.str("66b8acfd5af7677ee4ca05ff37863066")

db_type = env.str("DATABASE_TYPE")
db_url = env.str("DATABASE_URL", "")
db_name = env.str("DATABASE_NAME")

test_server = env.bool("TEST_SERVER", False)
modules_repo_branch = env.str("MODULES_REPO_BRANCH", "master")
