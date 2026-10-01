---
layout: default
title: Cyproheptadine
parent: 高證據等級 (L1-L2)
nav_order: 232
evidence_level: L2
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

# Cyproheptadine：從過敏性症狀到冷型蕁麻疹

## 一句話總結

Cyproheptadine 是第一代 H1 抗組織胺藥，在香港已上市，目前登記資料未載明原適應症。
TxGNN 模型預測它可能對**冷型蕁麻疹 (Cold Urticaria)** 有效（排名第 2 的預測），
目前有 **0 個直接相關臨床試驗**，但有 **數篇直接研究 cyproheptadine 的文獻**（含 2 篇雙盲對照研究）支持這個方向。

> 說明：排名第 1 的預測為過敏性蕁麻疹 (allergic urticaria)，但其證據皆為同類藥物（loratadine、desloratadine 等），並無 cyproheptadine 的直接研究。本報告以證據最完整的冷型蕁麻疹為主要評估對象，並在文末列出其他預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 冷型蕁麻疹 (Cold Urticaria) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據已知資訊，Cyproheptadine 是第一代 H1 抗組織胺藥，並兼具抗血清素 (5-HT2) 與抗膽鹼作用。

冷型蕁麻疹是由肥大細胞釋放組織胺所介導的疾病，遇冷後出現風疹塊與血管性水腫。H1 受體阻斷在機轉上與此病理相符，抗血清素作用也可能有額外貢獻。

這是四個預測中唯一有 cyproheptadine 直接臨床證據的適應症。多項雙盲、對照研究（1977–1995 年）將 cyproheptadine 與 chlorpheniramine、ketotifen、cinnarizine、doxepin、hydroxyzine 等藥物比較，其中一項為兒童研究。不過這些研究年代久遠、樣本數小，且目前指引多偏好使用第二代抗組織胺（如高劑量 desloratadine）。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | RCT（雙盲） | Arch Dermatol | 8 位原發性後天性冷型蕁麻疹患者，比較 cyproheptadine、chlorpheniramine 與安慰劑（各 4 mg，每日 3 次） |
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | 隨機雙盲比較研究 | J Am Acad Dermatol | 比較 cinnarizine、cyproheptadine、doxepin、hydroxyzine；以冰塊試驗評估，doxepin 表現較佳 |
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | 雙盲交叉試驗 | Dermatologica | 18 位患者；acrivastine 與 cyproheptadine 皆顯著優於安慰劑，acrivastine 效果更佳 |
| [6102102](https://pubmed.ncbi.nlm.nih.gov/6102102/) | 1980 | 臨床研究 | J Allergy Clin Immunol | 服用 cyproheptadine 後患者無症狀，冰塊試驗恢復正常，6 位中僅 1 位在冰水浸泡後出現腫脹 |
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | 雙盲交叉研究（兒童） | Asian Pac J Allergy Immunol | 6 位泰國兒童，比較 cyproheptadine 與 ketotifen 的療效 |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | 臨床研究（兒童） | Asian Pac J Allergy Immunol | 兒童冰塊試驗；cyproheptadine 治療四週後，冰塊試驗陽性率下降 |
| [5287036](https://pubmed.ncbi.nlm.nih.gov/5287036/) | 1971 | 臨床研究 | J Allergy Clin Immunol | 以 cyproheptadine 治療冷型蕁麻疹的早期報告（無摘要） |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT（間接） | J Allergy Clin Immunol | 高劑量 desloratadine 可降低風疹塊體積並改善冷刺激閾值 |
| [8447871](https://pubmed.ncbi.nlm.nih.gov/8447871/) | 1993 | Review | Am J Emerg Med | 冷誘發蕁麻疹與血管性水腫的診斷與處置 |
| [3760401](https://pubmed.ncbi.nlm.nih.gov/3760401/) | 1986 | 世代研究／回顧 | J Allergy Clin Immunol | 50 位患者中 70% 曾發生冷誘發的全身性反應，提出預防建議與診斷分類 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-17900 | CYPROHEPTADINE TAB 4MG | 未載明 | 未載明 |
| HK-05079 | CYPROHEPTADINE TAB 4MG (SYNCO) | 未載明 | 未載明 |
| HK-21862 | APPETIN SYRUP 2MG/5ML | 未載明 | 未載明 |
| HK-11455 | CYPROHEPTADINE SYRUP 2MG/5ML | 未載明 | 未載明 |
| HK-46023 | CYPRODIN TAB 4MG | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢未找到資料。
依第一代抗組織胺的藥物特性，使用時需留意鎮靜、抗膽鹼作用及兒童用藥安全（此為類別層級的提醒，並非來自本次資料包的仿單內容）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
冷型蕁麻疹是四個預測中唯一有 cyproheptadine 直接臨床研究的適應症，包含多項雙盲對照研究。但這些研究年代久遠、樣本很小，且目前多偏好第二代抗組織胺，因此僅適合帶著防護條件推進。

**若要推進需要：**
- 取得上述研究全文，核對設計、樣本數與療效指標（目前僅依標題與部分摘要評估）
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症（許可證資料中適應症皆為空白）
- 補齊 DrugBank 的作用機轉資料
- 與第二代抗組織胺（如高劑量 desloratadine）做療效與安全性比較
- 規劃鎮靜、抗膽鹼作用與兒童族群的監測

---

## 其他預測適應症（參考）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----|-----------|-----------|---------|------|
| 1 | 過敏性蕁麻疹 (Allergic Urticaria) | 99.96% | L4 | Research Question：證據皆為同類藥物（loratadine、desloratadine、rupatadine、bilastine 等），無 cyproheptadine 直接研究 |
| 3 | 鼻腔疾病 (Nasal Cavity Disease) | 99.21% | L4 | Hold：疾病定義不明確，主要反映過敏性鼻炎，且無 cyproheptadine 相關證據，建議先縮小適應症範圍 |
| 4 | 急性喉咽炎 (Acute Laryngopharyngitis) | 99.13% | L5 | Hold：僅有模型預測，無試驗與文獻；抗膽鹼的乾燥作用甚至可能不利 |

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

