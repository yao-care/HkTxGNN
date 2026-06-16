---
layout: default
title: Desloratadine
parent: 高證據等級 (L1-L2)
nav_order: 218
evidence_level: L1
indication_count: 6
---

# Desloratadine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Desloratadine：從過敏性疾病到冷蕁麻疹

## 一句話總結

Desloratadine 是一種強效的第二代 H1 受體拮抗劑，廣泛用於過敏性鼻炎及蕁麻疹症狀緩解，在香港目前尚無核准上市登記。
TxGNN 模型預測它可能對**冷蕁麻疹 (Cold Urticaria)** 有效，
目前有 **3 個臨床試驗**和 **7 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性疾病（香港無核准登記） |
| 預測新適應症 | 冷蕁麻疹（Cold Urticaria） |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）文件資料。根據已知資訊，Desloratadine 是一種**強效選擇性第二代 H1 受體拮抗劑**，為 Loratadine 的活性代謝物，其在過敏症狀治療中的療效已有充分臨床驗證。

冷蕁麻疹的發病機制為冷刺激誘發肥大細胞與嗜鹼性球脫顆粒，大量釋放組胺，直接驅動皮膚風團與潮紅反應。Desloratadine 透過阻斷 H1 受體，可有效抑制血管通透性增加及感覺神經激活，在機制上與冷蕁麻疹的核心病理直接對應。

此外，Desloratadine 具有 NF-κB 抑制及抗細胞激素活性（抑制 IL-4、IL-6 等），進一步強化其對冷蕁麻疹的療效機轉，使得 TxGNN 的預測具有高度生物學合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | 完成 | 33 | 隨機雙盲安慰劑對照交叉設計，比較 5mg vs 20mg desloratadine 對冷蕁麻疹皮損的抑制效果（熱影像、容積測量），評估高劑量是否優於標準劑量 |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | 完成 | 150 | 多中心研究，直接比較含 desloratadine 在內的 5 種抗組胺藥抑制蕁麻疹反應的藥效動力學與臨床療效，具比較效益數據 |
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | 完成 | 30 | 多中心雙盲劑量爬升研究（5mg / 10mg / 20mg），評估 desloratadine 在後天性冷蕁麻疹患者中的最適劑量與劑量效應關係 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | 高劑量 desloratadine 與標準劑量相比，顯著縮小風團體積並改善後天性冷蕁麻疹患者的冷激發閾值，支持劑量加倍策略 |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | H1 抗組胺藥劑量爬升的隨機對照試驗，以臨界溫度閾值量化治療反應，顯示劑量與療效存在相關性 |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Clinical RCT | J Dermatol Treat | 12 名冷蕁麻疹患者以 5mg desloratadine 治療 4 天，冰塊激發試驗前後對比，確認 desloratadine 可有效抑制冷蕁麻疹反應 |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | 慢性蕁麻疹病因與管理的系統性綜述，H1 抗組胺藥（含 desloratadine）為第一線治療，並討論高劑量策略 |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Comparative Review | Allergy | 第二代抗組胺藥於過敏性鼻炎與慢性蕁麻疹治療的比較綜述，提供 desloratadine 同類藥物療效脈絡 |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case Series | J Allergy Clin Immunol Pract | 食物依賴型冷蕁麻疹新亞型描述，擴展冷蕁麻疹的臨床分類，並討論抗組胺藥的管理角色 |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case Report | Qatar Med J | 首例黑蟻叮咬誘發過敏反應後繼發後天性冷蕁麻疹的病例報告，記錄罕見誘發機制 |

---

## 香港上市資訊

香港目前無 Desloratadine 核准上市許可證登記。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
冷蕁麻疹的發病機制（冷刺激→組胺釋放）與 Desloratadine 的 H1 阻斷機制高度吻合，且有 3 個已完成的 Phase 4 隨機對照試驗（含劑量優化研究）及多篇 RCT 文獻直接支持，證據等級達 L1，為在同類適應症中罕見的高質量直接證據。

**若要推進需要：**
- 補充正式藥物作用機轉（MOA）文件（建議查詢 DrugBank API）
- 取得香港（衛生署）及相關監管機構的安全性仿單資料（警語、禁忌、DDI）
- 評估香港本地患者的劑量調整策略（標準 5mg vs 高劑量 20mg）
- 確認本地注冊及進口申請路徑（香港衛生署藥劑業及毒藥管理局）

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用於實際診療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

