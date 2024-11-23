class COOLIFY_BUILD_PACKS:
    """
    Coolify build packs types.
    """
    nixpacks = "nixpacks"
    static = "static"
    dockerfile = "dockerfile"
    dockercompose = "dockercompose"


class COOLIFY_REDIRECT:
    """
    Coolify web redirect types.
    """
    www = "www"
    non_www = "non-www"
    both = "both"


class COOLIFY_PROXY_TYPES:
    """
    Coolify proxy types.
    """
    traefik = "traefik"
    caddy = "caddy"




class COOLIFY_SERVICE_TYPES:
    """
    Coolify services types.
    """
    activepieces = "activepieces"
    appsmith = "appsmith"
    appwrite = "appwrite"
    authentik = "authentik"
    babybuddy = "babybuddy"
    budge = "budge"
    changedetection = "changedetection"
    chatwoot = "chatwoot"
    classicpress_with_mariadb = "classicpress-with-mariadb"
    classicpress_with_mysql = "classicpress-with-mysql"
    classicpress_without_database = "classicpress-without-database"
    cloudflared = "cloudflared"
    code_server = "code-server"
    dashboard = "dashboard"
    directus = "directus"
    directus_with_postgresql = "directus-with-postgresql"
    docker_registry = "docker-registry"
    docuseal = "docuseal"
    docuseal_with_postgres = "docuseal-with-postgres"
    dokuwiki = "dokuwiki"
    duplicati = "duplicati"
    emby = "emby"
    embystat = "embystat"
    fider = "fider"
    filebrowser = "filebrowser"
    firefly = "firefly"
    formbricks = "formbricks"
    ghost = "ghost"
    gitea = "gitea"
    gitea_with_mariadb = "gitea-with-mariadb"
    gitea_with_mysql = "gitea-with-mysql"
    gitea_with_postgresql = "gitea-with-postgresql"
    glance = "glance"
    glances = "glances"
    glitchtip = "glitchtip"
    grafana = "grafana"
    grafana_with_postgresql = "grafana-with-postgresql"
    grocy = "grocy"
    heimdall = "heimdall"
    homepage = "homepage"
    jellyfin = "jellyfin"
    jenkins = "jenkins"
    kuzzle = "kuzzle"
    listmonk = "listmonk"
    logto = "logto"
    mediawiki = "mediawiki"
    meilisearch = "meilisearch"
    metabase = "metabase"
    metube = "metube"
    minio = "minio"
    moodle = "moodle"
    mosquitto = "mosquitto"
    n8n = "n8n"
    n8n_with_postgresql = "n8n-with-postgresql"
    next_image_transformation = "next-image-transformation"
    nextcloud = "nextcloud"
    nocodb = "nocodb"
    odoo = "odoo"
    openblocks = "openblocks"
    pairdrop = "pairdrop"
    penpot = "penpot"
    phpmyadmin = "phpmyadmin"
    pocketbase = "pocketbase"
    posthog = "posthog"
    reactive_resume = "reactive-resume"
    rocketchat = "rocketchat"
    shlink = "shlink"
    slash = "slash"
    snapdrop = "snapdrop"
    statusnook = "statusnook"
    stirling_pdf = "stirling-pdf"
    supabase = "supabase"
    syncthing = "syncthing"
    tolgee = "tolgee"
    trigger = "trigger"
    trigger_with_external_database = "trigger-with-external-database"
    twenty = "twenty"
    umami = "umami"
    unleash_with_postgresql = "unleash-with-postgresql"
    unleash_without_database = "unleash-without-database"
    uptime_kuma = "uptime-kuma"
    vaultwarden = "vaultwarden"
    vikunja = "vikunja"
    weblate = "weblate"
    whoogle = "whoogle"
    wordpress_with_mariadb = "wordpress-with-mariadb"
    wordpress_with_mysql = "wordpress-with-mysql"
    wordpress_without_database = "wordpress-without-database"



class URL_MAP:
    """
    Coolipy URL map.
    """
    version = "/version"
    servers = "/servers"
    projects = "/projects"
    deployments = "/deployments"
    deploy = "/deploy"
    resources = "/resources"
    private_keys = "/security/keys"
    health = "/health"
    enable = "/enable"
    disable = "/disable"
    teams = "/teams"
    services = "/services"
    databases = "/databases"
    applications = "/applications"
    start = "/start"
    stop = "/stop"
    restart = "/restart"
    execute = "/execute"
    envs = "/envs"
    bulk = "/bulk"
    domains = "/domains"
    validate = "/validate"
    members = "/members"
    current = "/current"


API_BASE_ENTRYPOINT = "/api/v1"
COOLIFY_DEFAULT_PROXY = "traefik"


COOLIFY_DEFAULT_PROXY = COOLIFY_PROXY_TYPES.traefik


class COOLIFY_RETURN_TYPES:
    list = "list"
    single = "single"
    raw = "raw"

