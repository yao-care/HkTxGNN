---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 949
evidence_level: L5
indication_count: 6
monitor_inn: "ZANUBRUTINIB"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "Ewing sarcoma", "neuroblastoma"]
last_modified_at: 2026-10-23
description: "Zanubrutinib：預測新適應症為骨髓性白血病（證據等級 L5）。原適應症：香港許可證未登載適應症文字"
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Zanubrutinib：從套細胞淋巴瘤到骨髓性白血病
{: .text-alpha }

## 一句話總結

Zanubrutinib 是一種 BTK 抑制劑，知識圖譜中記錄的相關疾病包括套細胞淋巴瘤、B 細胞腫瘤與淋巴肉瘤。
TxGNN 模型預測它可能對**骨髓性白血病 (myeloid leukemia)** 有效，但目前**沒有直接研究此疾病的臨床試驗或文獻**，證據僅屬模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未登載適應症文字；知識圖譜中記錄的關聯為套細胞淋巴瘤、B 細胞腫瘤、淋巴肉瘤（屬知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 骨髓性白血病 |
| TxGNN 預測分數 | 0.9965 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Zanubrutinib 是選擇性、共價結合的 BTK 抑制劑，BTK 訊號在 B 細胞惡性腫瘤（慢性淋巴球性白血病/小淋巴球淋巴瘤、套細胞淋巴瘤、華氏巨球蛋白血症）中已有文獻支持其角色。

至於骨髓性白血病，證據是間接的。有研究提到 BTK 在骨髓系細胞中表現，可能與急性骨髓性白血病細胞的存活及微環境訊號有關，但這只是假說，本報告所整理的資料並未證實。TxGNN 的高分（0.9965）很可能來自藥物與白血病、淋巴惡性腫瘤的整體關聯，不能解讀為對骨髓性白血病有專一支持。現有資料並未顯示 zanubrutinib 在骨髓性白血病中有活性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | 完成 | 86 | 評估 CDK9 抑制劑 PRT2527 單用或與 zanubrutinib、venetoclax 合併，用於復發/難治性血液惡性腫瘤的安全性與初步療效；zanubrutinib 僅為合併用藥，無法直接佐證其對骨髓性白血病的效果 |

## 文獻證據

以下文獻皆未直接研究骨髓性白血病，主要涵蓋 B 細胞惡性腫瘤（如 CLL/SLL）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 試驗 5 年追蹤：初治 CLL/SLL 中 zanubrutinib 對比 bendamustine + rituximab |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | 單臂 Phase 2 試驗 | Lancet Haematol | 對先前 BTK 抑制劑不耐受的 B 細胞惡性腫瘤患者，評估 zanubrutinib 的安全性與活性 |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | 臨床試驗更新 | Blood Adv | 對 ibrutinib/acalabrutinib 不耐受的 CLL/SLL，zanubrutinib 耐受性與療效更新 |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | 合併分析 | Blood Adv | 具 del(17p)/TP53 異常的 CLL/SLL 中，zanubrutinib 跨試驗療效與安全性分析 |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | 慢性白血病（CML、CLL）酪胺酸激酶抑制劑治療回顧 |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | BTK 抑制劑用於華氏巨球蛋白血症的治療 |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review/安全性分析 | Clin Lymphoma Myeloma Leuk | 接受 BTK 抑制劑患者的 B 型肝炎病毒再活化 |
| [42192981](https://pubmed.ncbi.nlm.nih.gov/42192981/) | 2026 | Review | Cancers | CLL 中 BTK 抑制劑的低免疫球蛋白血症與感染風險 |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | 華氏巨球蛋白血症併 B 細胞急性淋巴母細胞白血病的罕見病例 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67529 | BRUKINSA CAPSULES 80MG | 未載明 | 未載明 |

## 細胞毒性

Zanubrutinib 屬標靶藥物（BTK 抑制劑），非傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（BTK 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分重要項目：
  - 嚴重（Major）：Aprepitant、乙醯水楊酸（阿斯匹靈）、Dexamethasone、Clarithromycin、Cobicistat、Deferasirox、Deferiprone、Ibritumomab tiuxetan 等
  - 中度（Moderate）：Cimetidine、Miconazole、Clotrimazole、Fenfluramine 等
- **其他注意事項**：文獻指出 BTK 抑制劑可能與 B 型肝炎病毒再活化、低免疫球蛋白血症及感染風險增加有關。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接評估 zanubrutinib 於骨髓性白血病，唯一相關試驗中它僅是合併用藥，故證據等級為 L5，僅有模型預測。
- 高 TxGNN 分數很可能反映藥物與淋巴惡性腫瘤的關聯，而非骨髓性白血病專一的證據。

**若要推進需要：**
- 補充 BTK 在骨髓性白血病（含 AML 亞型）的機轉與前臨床證據
- 取得 zanubrutinib 於骨髓性白血病的直接臨床或前臨床研究資料
- 取得香港原廠仿單的核准適應症、警語與禁忌症
- 釐清 NCT05665530 各組別設計，確認 zanubrutinib 的角色
- 排定合併用藥（如強效 CYP3A 抑制劑、抗血小板藥物）的交互作用管理策略
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

