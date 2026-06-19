import json
import sys
from datetime import datetime

# 内置站点资料数据，包含关键词、URL、标签和简短说明
SITE_DATA = [
    {
        "keyword": "爱游戏",
        "url": "https://site-m-i-game.com.cn",
        "tags": ["游戏", "娱乐", "平台"],
        "description": "提供丰富的在线游戏与互动娱乐体验的综合平台。"
    },
    {
        "keyword": "爱游戏攻略",
        "url": "https://site-m-i-game.com.cn/guides",
        "tags": ["攻略", "技巧", "教程"],
        "description": "汇集各类热门游戏的详尽攻略与实用技巧。"
    },
    {
        "keyword": "爱游戏社区",
        "url": "https://site-m-i-game.com.cn/community",
        "tags": ["社区", "论坛", "交流"],
        "description": "玩家交流心得、分享经验、组队互动的活跃社区。"
    },
    {
        "keyword": "爱游戏活动",
        "url": "https://site-m-i-game.com.cn/events",
        "tags": ["活动", "福利", "赛事"],
        "description": "定期推出精彩线上活动、福利礼包与竞技赛事。"
    },
    {
        "keyword": "爱游戏下载",
        "url": "https://site-m-i-game.com.cn/download",
        "tags": ["下载", "客户端", "安装"],
        "description": "提供游戏客户端及配套工具的官方下载入口。"
    }
]

def compute_summary_stats(data):
    """计算摘要统计信息"""
    total = len(data)
    unique_tags = set()
    keyword_lengths = []
    for item in data:
        unique_tags.update(item.get("tags", []))
        keyword_lengths.append(len(item.get("keyword", "")))
    return {
        "total_sites": total,
        "unique_tags": sorted(unique_tags),
        "avg_keyword_length": round(sum(keyword_lengths) / max(total, 1), 2)
    }

def format_site_entry(index, item):
    """格式化单个站点条目"""
    tags_str = ", ".join(item.get("tags", []))
    return (
        f"  [{index}] 关键词: {item['keyword']}\n"
        f"       URL: {item['url']}\n"
        f"       标签: {tags_str}\n"
        f"       说明: {item['description']}\n"
    )

def build_structured_summary(data):
    """构建结构化摘要文本"""
    lines = []
    lines.append("=" * 64)
    lines.append("  站点资料结构化摘要")
    lines.append(f"  生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 64)
    lines.append("")

    stats = compute_summary_stats(data)
    lines.append(f"【概览】")
    lines.append(f"  站点总数: {stats['total_sites']}")
    lines.append(f"  唯一标签: {', '.join(stats['unique_tags'])}")
    lines.append(f"  关键词平均长度: {stats['avg_keyword_length']}")
    lines.append("")

    lines.append("【站点列表】")
    for i, item in enumerate(data, start=1):
        lines.append(format_site_entry(i, item))

    lines.append("【标签索引】")
    tag_sites = {}
    for item in data:
        for tag in item.get("tags", []):
            tag_sites.setdefault(tag, []).append(item["keyword"])
    for tag in sorted(tag_sites.keys()):
        sites = ", ".join(tag_sites[tag])
        lines.append(f"  {tag}: {sites}")
    lines.append("")
    lines.append("=" * 64)
    return "\n".join(lines)

def save_summary_to_file(content, filepath="site_summary_output.txt"):
    """将摘要写入文本文件"""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"摘要已保存至: {filepath}"
    except IOError as e:
        return f"保存文件失败: {e}"

def main():
    summary = build_structured_summary(SITE_DATA)
    print(summary)
    msg = save_summary_to_file(summary)
    print(msg)
    return 0

if __name__ == "__main__":
    sys.exit(main())