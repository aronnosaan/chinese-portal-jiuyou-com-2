SITE_DATA = {
    "portal": {
        "url": "https://chinese-portal-jiuyou.com",
        "keywords": ["九游", "中文门户", "游戏社区", "玩家论坛"],
        "tags": ["门户", "游戏", "中文", "社区"],
        "description": "九游中文门户，提供游戏资讯、攻略分享与玩家互动服务"
    },
    "news": {
        "url": "https://chinese-portal-jiuyou.com/news",
        "keywords": ["九游新闻", "游戏动态", "行业资讯", "更新公告"],
        "tags": ["新闻", "动态", "更新"],
        "description": "九游平台最新游戏新闻与行业动态"
    },
    "community": {
        "url": "https://chinese-portal-jiuyou.com/community",
        "keywords": ["九游社区", "玩家交流", "攻略讨论", "组队招募"],
        "tags": ["社区", "交流", "攻略"],
        "description": "九游玩家社区，自由讨论游戏策略与组队玩法"
    }
}

def generate_summary(site_name: str, data: dict) -> str:
    lines = []
    lines.append(f"站点名称: {site_name}")
    lines.append(f"URL: {data['url']}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"标签: {', '.join(data['tags'])}")
    lines.append(f"简短说明: {data['description']}")
    lines.append("-" * 40)
    return "\n".join(lines)

def build_full_report() -> str:
    header = "九游站点结构化摘要报告\n" + "=" * 40
    parts = [header]
    for site_name, site_info in SITE_DATA.items():
        parts.append(generate_summary(site_name, site_info))
    return "\n".join(parts)

if __name__ == "__main__":
    report = build_full_report()
    print(report)