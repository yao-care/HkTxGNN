---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Oxaliplatin：從原適應症（資料未提供）到惡性胸膜間皮瘤

## 一句話總結

Oxaliplatin（奧沙利鉑）是鉑類細胞毒性化療藥物，本次資料中未提供其原適應症。
TxGNN 模型預測它可能對**惡性胸膜間皮瘤 (Malignant Pleural Mesothelioma)** 有效。
目前有 **5 個相關臨床試驗登記**（其中 2 個直接以間皮瘤為對象）和 **20 篇文獻**，但都是小型單臂 Phase II 或回顧性資料，沒有隨機對照試驗（RCT）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 惡性胸膜間皮瘤 (Malignant Pleural Mesothelioma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L3（依判定規則；資料包自評為 L2，但現有 Phase II 皆為單臂，非 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Oxaliplatin 屬於鉑類化療藥物，一般認為它會與 DNA 形成加成物並造成交聯，阻礙 DNA 複製並誘發細胞凋亡。以下機轉推論來自藥物類別，不是直接的機轉資料。

惡性胸膜間皮瘤目前的標準一線治療是 pemetrexed 加鉑類（通常為 cisplatin）。Oxaliplatin 與 cisplatin 同屬鉑類，因此被視為可能的鉑類替代選項，而不是全新的作用機轉。單臂 Phase II 研究顯示，oxaliplatin 合併 gemcitabine 或 raltitrexed 在間皮瘤中有一定活性。

TxGNN 的高分（0.997）與這些臨床訊號方向一致，但它本身不提供獨立證據。另一項小型研究顯示 raltitrexed + oxaliplatin 作為二線治療沒有客觀反應，這代表療效在不同治療階段並不一致。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | 完成 | 29 | Oxaliplatin + gemcitabine 用於惡性胸膜或腹膜間皮瘤（一線或二線），主要評估反應率；單臂、規模小，直接相關 |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | 未知 | 29 | Bortezomib + oxaliplatin 用於曾接受治療的胸膜或腹膜間皮瘤；輸入資料中無結果，且標題被截斷，適應症由檢索比對推定 |
| [NCT07330271](https://clinicaltrials.gov/study/NCT07330271) | N/A | 招募中 | 347 | 以病人來源腫瘤培養引導個人化治療的隨機試驗（腹膜間皮瘤）；測試的是選藥策略，不是 oxaliplatin 本身 |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | 未知 | 1000 | PIPAC/PITAC 加壓氣霧化腹腔化療的國際登錄；混合藥物，與胸膜間皮瘤關聯低 |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | 招募中 | 345 | CBL-B 抑制劑 NX-1607 的首次人體試驗；研究藥物非 oxaliplatin，關聯低 |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | 尚未招募 | 30 | 新輔助 cadonilimab 加化療用於食道胃交界及胃癌；疾病不符，可能只是偶然比對 |

## 文獻證據

本次沒有 RCT。以下依研究直接性排序：先是間皮瘤中的 oxaliplatin 臨床研究，再是回顧文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase II（raltitrexed + oxaliplatin） | J Clin Oncol | 開放性研究，納入 70 位瀰漫性胸膜間皮瘤病人（15 位曾治療、55 位未治療），標題結論為「活性療法」 |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase II（多中心、單臂） | Clin Lung Cancer | 25 位病人接受 gemcitabine + oxaliplatin，最多 6 個週期，評估活性 |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase II 先導研究 | Tumori | Oxaliplatin + raltitrexed 用於無法手術的胸膜間皮瘤；此前 Phase I 已顯示有活性 |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase II | Lung Cancer | Vinorelbine + oxaliplatin 作為未治療胸膜間皮瘤的一線治療 |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase II | Lung Cancer | Raltitrexed + oxaliplatin 二線治療：14 位病人無客觀反應，僅 4 位（28.6%）病情穩定，試驗提前終止（負面結果） |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | 觀察性研究 | J Occup Med Toxicol | Gemcitabine ± oxaliplatin 用於曾接受 pemetrexed 治療的病人，評估療效與安全性 |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sci | 探討 cisplatin、oxaliplatin、pemetrexed 對免疫檢查點表現的影響，作為與免疫治療合併的依據 |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | 整理間皮瘤化療結果；傳統藥物反應率難超過 30%，新藥與組合較有希望 |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | 抗葉酸藥物在間皮瘤的角色，提到 raltitrexed/oxaliplatin 為新興組合之一 |
| [15261443](https://pubmed.ncbi.nlm.nih.gov/15261443/) | 2004 | Review | Lung Cancer | 彙整 Phase II-III 化療研究，指出新型藥物與組合較有前景 |

## 香港上市資訊

共 18 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症文字，故省略這兩欄。

| 許可證號 | 品名 | 製造商／持證商 |
|---------|------|---------------|
| HK-63464 | OXALIPLATIN HOSPIRA CONCENTRATE FOR SOLUTION FOR INFUSION 50MG/10ML | PFIZER CORPORATION HONG KONG LIMITED |
| HK-67490 | OXACCORD CONCENTRATE FOR SOLUTION FOR INFUSION 50MG/10ML | JACOBSON MARKETING LIMITED |
| HK-60056 | OXALIPLATIN FOR INJ 50MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-67993 | OXALIPLATIN ADVAGEN CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/20ML | ADVAGEN (H.K.) LIMITED |
| HK-67689 | DIOXOFIN CONCENTRATE FOR SOLUTION FOR INFUSION 200MG/40ML | THE INTERNATIONAL MEDICAL COMPANY LIMITED |

## 細胞毒性

以下依藥物類別判斷，資料包未提供 DrugBank 毒性資料，實際請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（鉑類） |
| 骨髓抑制風險 | 中（鉑類化療常見血球下降） |
| 致吐性分級 | 中 |
| 監測項目 | CBC（含分類）、肝腎功能、電解質；另需追蹤周邊神經病變症狀（鉑類常見的劑量限制毒性） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有小型單臂 Phase II 和回顧性資料，沒有 RCT，且已有一項二線研究顯示無客觀反應。標準一線治療 pemetrexed + 鉑類已存在，oxaliplatin 較像 cisplatin 的替代選項，沒有新機轉。
- 香港仿單的警語與禁忌資料缺口被標為 Blocking，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症），補齊安全性資料
- 從 DrugBank 補充作用機轉與毒性資料
- 確認 NCT00859469 與 NCT00996385 是否已有發表結果，並核實後者的疾病適應症
- 與現行標準治療（pemetrexed + cisplatin）做比較，評估 oxaliplatin 的定位，例如用於無法耐受 cisplatin 的病人
- 另有三個預測適應症：上皮樣間皮瘤（L3，證據多為腹膜疾病的腹腔內給藥）、肉瘤樣間皮瘤（L4，Hold）、惡性臟層胸膜腫瘤（L4，Hold，建議與胸膜間皮瘤合併看待）。這幾項證據都比本報告的主要適應症更弱。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

