#!/usr/bin/env python3
"""
小红书敏感词/违禁词库
覆盖：广告法违禁词、医疗健康、金融理财、虚假宣传等
"""

# 广告法违禁词 - 极限用语
ADVERTISING_EXTREME_WORDS = [
    # 绝对化用语
    "最", "最佳", "最好", "最优", "最高", "最低", "最大", "最小", "最强", "最新",
    "第一", "唯一", "首个", "首选", "独家", "独一无二", "绝无仅有", "史无前例",
    "顶级", "顶尖", "极致", "极品", "终极", "至尊", "王牌", "冠军", "领袖", "领导者",
    "NO.1", "No.1", "TOP1", "销量第一", "销量冠军", "行业第一", "全网第一",
    "世界级", "国家级", "全球首发", "全国首创", "独创", "首创",
    "100%", "百分百", "纯天然", "零添加", "零风险", "零副作用",
    "永久", "永恒", "万能", "全能", "无敌", "无限",
    
    # 虚假承诺
    "保证", "承诺", "必须", "肯定", "一定", "绝对",
    "包治", "包好", "包退", "包换", "包赔",
    "立即见效", "立竿见影", "药到病除", "一次见效", "当天见效",
    "无效退款", "假一赔十", "假一赔百",
]

# 医疗健康违禁词
MEDICAL_WORDS = [
    # 疾病治疗相关
    "治疗", "治愈", "根治", "痊愈", "康复", "疗效", "药效",
    "抗癌", "防癌", "抗肿瘤", "消炎", "杀菌", "抑菌", "灭菌",
    "降血压", "降血糖", "降血脂", "降胆固醇",
    "补肾", "壮阳", "丰胸", "减肥", "瘦身", "燃脂", "排毒", "祛斑", "祛痘",
    "抗衰老", "抗氧化", "延缓衰老", "逆龄", "冻龄",
    
    # 医疗机构/资质
    "处方", "医院", "诊所", "门诊", "专家", "名医", "神医",
    "临床验证", "临床试验", "医学证明", "科学验证",
    
    # 药品相关
    "药品", "药物", "中药", "西药", "特效药", "神药", "祖传秘方", "偏方",
    "保健品", "营养品", "功能性食品",
    
    # 身体部位功效
    "改善睡眠", "助眠", "安神", "镇静",
    "增强免疫力", "提高免疫力", "增强体质",
    "调节内分泌", "调理身体", "调理肠胃",
]

# 金融理财违禁词
FINANCIAL_WORDS = [
    # 收益承诺
    "保本", "保息", "保收益", "稳赚", "稳赚不赔", "躺赚", "躺着赚钱",
    "高收益", "高回报", "超高收益", "年化收益", "日收益", "月收益",
    "翻倍", "翻番", "暴涨", "暴富", "一夜暴富", "财务自由",
    "零风险", "无风险", "低风险高收益",
    
    # 投资诱导
    "内幕", "内幕消息", "小道消息", "独家消息",
    "庄家", "主力", "跟庄", "抄底", "逃顶",
    "牛股", "黑马股", "涨停", "连续涨停",
    "稳赚", "必涨", "必赚", "包赚",
    
    # 非法金融
    "配资", "杠杆", "高杠杆", "场外配资",
    "虚拟货币", "数字货币", "代币", "ICO", "炒币",
    "传销", "拉人头", "下线", "返利", "分红",
    "贷款", "网贷", "小额贷", "无抵押贷款", "秒批", "秒下款",
]

# 虚假宣传违禁词
FALSE_ADVERTISING_WORDS = [
    # 虚假背书
    "央视推荐", "CCTV推荐", "国家认证", "政府推荐", "官方认证",
    "明星同款", "网红同款", "爆款", "断货王", "卖疯了",
    "销量突破", "好评如潮", "零差评", "全五星",
    
    # 虚假数据
    "万人验证", "百万用户", "千万用户", "亿万用户",
    "99%好评", "100%好评", "100%有效", "100%满意",
    
    # 诱导性用语
    "限时", "限量", "秒杀", "抢购", "疯抢", "最后一天", "即将涨价",
    "错过再等一年", "手慢无", "售完即止", "库存告急",
    "免费", "0元", "白送", "白拿", "不要钱",
]

# 违规引流词
TRAFFIC_VIOLATION_WORDS = [
    # 私域引流
    "加微信", "加V", "加vx", "加wx", "私聊", "私信",
    "扫码", "二维码", "公众号", "小程序",
    "淘宝", "天猫", "京东", "拼多多", "闲鱼",
    
    # 违规变现
    "代购", "代理", "招代理", "招商", "加盟",
    "兼职", "副业", "赚钱", "创业", "致富",
]

# 敏感政治词汇（简化版，实际使用需要更完整的词库）
POLITICAL_WORDS = [
    "国家领导人", "政治敏感", "敏感事件",
]

# 低俗违规词
VULGAR_WORDS = [
    "色情", "赌博", "毒品", "暴力", "血腥",
    "约炮", "一夜情", "援交", "小姐",
]

# 小红书特定违禁词
XIAOHONGSHU_SPECIFIC_WORDS = [
    # 引流相关
    "关注我", "点赞", "收藏", "转发", "评论区",
    "私信我", "滴滴我", "dd我", "戳我主页",
    
    # 营销相关
    "好物推荐", "必买", "必入", "闭眼入", "无脑入",
    "回购无数次", "空瓶记", "真实测评",
]


def get_all_sensitive_words():
    """获取所有敏感词列表"""
    all_words = []
    all_words.extend(ADVERTISING_EXTREME_WORDS)
    all_words.extend(MEDICAL_WORDS)
    all_words.extend(FINANCIAL_WORDS)
    all_words.extend(FALSE_ADVERTISING_WORDS)
    all_words.extend(TRAFFIC_VIOLATION_WORDS)
    all_words.extend(POLITICAL_WORDS)
    all_words.extend(VULGAR_WORDS)
    all_words.extend(XIAOHONGSHU_SPECIFIC_WORDS)
    
    # 去重并返回
    return list(set(all_words))


def get_sensitive_words_by_category():
    """按分类获取敏感词"""
    return {
        "advertising": {
            "name": "广告法违禁词",
            "words": ADVERTISING_EXTREME_WORDS,
            "color": "#ff4d4f"  # 红色
        },
        "medical": {
            "name": "医疗健康",
            "words": MEDICAL_WORDS,
            "color": "#fa8c16"  # 橙色
        },
        "financial": {
            "name": "金融理财",
            "words": FINANCIAL_WORDS,
            "color": "#faad14"  # 黄色
        },
        "false_advertising": {
            "name": "虚假宣传",
            "words": FALSE_ADVERTISING_WORDS,
            "color": "#eb2f96"  # 粉色
        },
        "traffic": {
            "name": "违规引流",
            "words": TRAFFIC_VIOLATION_WORDS,
            "color": "#722ed1"  # 紫色
        },
        "political": {
            "name": "政治敏感",
            "words": POLITICAL_WORDS,
            "color": "#1890ff"  # 蓝色
        },
        "vulgar": {
            "name": "低俗违规",
            "words": VULGAR_WORDS,
            "color": "#f5222d"  # 深红色
        },
        "xiaohongshu": {
            "name": "小红书特定",
            "words": XIAOHONGSHU_SPECIFIC_WORDS,
            "color": "#13c2c2"  # 青色
        }
    }


def detect_sensitive_words(text):
    """
    检测文本中的敏感词
    
    Args:
        text: 待检测的文本
        
    Returns:
        dict: {
            "has_sensitive": bool,  # 是否包含敏感词
            "total_count": int,     # 敏感词总数
            "details": [            # 详细信息
                {
                    "word": str,        # 敏感词
                    "category": str,    # 分类
                    "category_name": str,  # 分类名称
                    "color": str,       # 高亮颜色
                    "positions": [int]  # 出现位置
                }
            ],
            "summary": {            # 按分类汇总
                "category_key": {
                    "name": str,
                    "count": int,
                    "words": [str]
                }
            }
        }
    """
    if not text:
        return {
            "has_sensitive": False,
            "total_count": 0,
            "details": [],
            "summary": {}
        }
    
    categories = get_sensitive_words_by_category()
    details = []
    summary = {}
    found_words = set()
    
    # 转换为小写进行匹配（保留原文用于位置定位）
    text_lower = text.lower()
    
    # 收集所有敏感词并按长度排序（优先匹配长词）
    all_words_with_cat = []
    for cat_key, cat_info in categories.items():
        for word in cat_info["words"]:
            all_words_with_cat.append({
                "word": word,
                "cat_key": cat_key,
                "cat_info": cat_info
            })
    
    # 按词长度降序排序，优先匹配长词
    all_words_with_cat.sort(key=lambda x: len(x["word"]), reverse=True)
    
    # 记录已匹配的位置区间，避免重复匹配
    matched_ranges = []
    
    for item in all_words_with_cat:
        word = item["word"]
        cat_key = item["cat_key"]
        cat_info = item["cat_info"]
        word_lower = word.lower()
        
        # 查找所有出现位置
        positions = []
        start = 0
        while True:
            pos = text_lower.find(word_lower, start)
            if pos == -1:
                break
            
            # 检查该位置是否已被更长的词匹配
            end_pos = pos + len(word)
            is_overlapping = False
            for matched_start, matched_end in matched_ranges:
                if not (end_pos <= matched_start or pos >= matched_end):
                    is_overlapping = True
                    break
            
            if not is_overlapping:
                positions.append(pos)
                matched_ranges.append((pos, end_pos))
            
            start = pos + 1
        
        if positions:
            found_words.add(word)
            details.append({
                "word": word,
                "category": cat_key,
                "category_name": cat_info["name"],
                "color": cat_info["color"],
                "positions": positions
            })
            
            # 更新分类汇总
            if cat_key not in summary:
                summary[cat_key] = {
                    "name": cat_info["name"],
                    "count": 0,
                    "words": [],
                    "color": cat_info["color"]
                }
            summary[cat_key]["count"] += 1
            summary[cat_key]["words"].append(word)
    
    return {
        "has_sensitive": len(found_words) > 0,
        "total_count": len(found_words),
        "details": details,
        "summary": summary
    }


def highlight_sensitive_words(text, detection_result):
    """
    将敏感词高亮标记（返回 HTML 格式）
    
    Args:
        text: 原始文本
        detection_result: detect_sensitive_words 的返回结果
        
    Returns:
        str: 带有 HTML 高亮标记的文本
    """
    if not detection_result["has_sensitive"]:
        return text
    
    # 收集所有需要高亮的位置和信息
    highlights = []
    for detail in detection_result["details"]:
        word = detail["word"]
        color = detail["color"]
        for pos in detail["positions"]:
            highlights.append({
                "start": pos,
                "end": pos + len(word),
                "word": word,
                "color": color,
                "category_name": detail["category_name"]
            })
    
    # 按位置排序（从后往前替换，避免位置偏移）
    highlights.sort(key=lambda x: x["start"], reverse=True)
    
    # 处理重叠的高亮区域（保留较长的词）
    filtered_highlights = []
    for h in highlights:
        overlap = False
        for fh in filtered_highlights:
            if not (h["end"] <= fh["start"] or h["start"] >= fh["end"]):
                overlap = True
                break
        if not overlap:
            filtered_highlights.append(h)
    
    # 应用高亮
    result = text
    for h in filtered_highlights:
        original_word = result[h["start"]:h["end"]]
        highlighted = f'<span class="sensitive-word" style="background-color: {h["color"]}; color: white; padding: 0 2px; border-radius: 2px;" title="{h["category_name"]}">{original_word}</span>'
        result = result[:h["start"]] + highlighted + result[h["end"]:]
    
    return result


if __name__ == "__main__":
    # 测试
    test_text = """
    这款产品是全网销量第一的爆款，100%纯天然成分，零添加零副作用。
    可以有效治疗各种皮肤问题，药到病除，一次见效！
    现在购买还能获得高收益理财产品推荐，稳赚不赔，年化收益30%！
    限时秒杀，最后一天，错过再等一年！加微信了解更多。
    """
    
    result = detect_sensitive_words(test_text)
    print(f"检测到 {result['total_count']} 个敏感词")
    print("\n按分类汇总：")
    for cat_key, cat_info in result["summary"].items():
        print(f"  {cat_info['name']}: {cat_info['count']} 个 - {', '.join(cat_info['words'])}")
    
    print("\n高亮后的文本：")
    print(highlight_sensitive_words(test_text, result))
