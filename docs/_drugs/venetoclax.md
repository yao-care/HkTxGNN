---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 930
evidence_level: L5
indication_count: 6
monitor_inn: "VENETOCLAX"
predicted_indications: ["Hodgkins lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
last_modified_at: 2026-10-28
description: "Venetoclax：預測新適應症為Hodgkins lymphoma（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Venetoclax
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

## Venetoclax: Hodgkins lymphoma
{: .text-alpha }

## 一句話總結

Venetoclax 是口服 BCL-2 抑制劑，知識圖譜記錄的原適應症關係為急性淋巴性白血病與 Richter 症候群。
TxGNN 模型預測它可能對**何杰金氏淋巴瘤 (Hodgkin's lymphoma)** 有效，但目前沒有任何研究直接針對此疾病，因此證據等級僅為 **L5**；支持證據多來自其他 B 細胞淋巴瘤。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Hodgkins lymphoma |
| TxGNN 預測分數 | 0.9951 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載。根據本報告彙整的資料，venetoclax 是選擇性 BCL-2 抑制劑，能恢復惡性 B 細胞的細胞凋亡能力。

古典型何杰金氏淋巴瘤對 BCL-2 的依賴程度低於慢性淋巴球性白血病、非何杰金氏淋巴瘤或被套細胞淋巴瘤，因此機轉上的連結合理但屬間接。此外，文獻指出 Richter 轉化偶爾可呈現何杰金氏淋巴瘤型態；TxGNN 模型（深度學習）的分數可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

TxGNN 的高分是計算預測，不能取代臨床證據。現有臨床資料多來自 B 細胞非何杰金氏淋巴瘤或混合型復發／難治性淋巴惡性腫瘤，缺乏何杰金氏淋巴瘤專屬研究。

## 臨床試驗證據

下列試驗皆未以何杰金氏淋巴瘤為專屬研究對象，僅列出最相關的淋巴瘤研究：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03223610](https://clinicaltrials.gov/study/NCT03223610) | Phase 1/2 | 招募中 | 155 | ViPOR 複方（venetoclax、ibrutinib、prednisone、obinutuzumab、lenalidomide）用於復發／難治性 B 細胞淋巴瘤，尚無何杰金氏專屬結果 |
| [NCT05371054](https://clinicaltrials.gov/study/NCT05371054) | Phase 1/2 | 完成 | 8 | VIP152＋venetoclax＋prednisone 用於復發／難治性淋巴惡性腫瘤，樣本極少 |
| [NCT03036904](https://clinicaltrials.gov/study/NCT03036904) | Phase 1 | 完成 | 31 | Venetoclax＋DA-EPOCH-R 用於侵襲性 B 細胞淋巴瘤，以 DLBCL 為主 |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | 完成 | 133 | Obinutuzumab／rituximab＋polatuzumab＋venetoclax 用於濾泡性淋巴瘤與 DLBCL，間接相關 |
| [NCT04447716](https://clinicaltrials.gov/study/NCT04447716) | Phase 1 | 進行中（不再招募） | 4 | Venetoclax＋lenalidomide＋rituximab 用於惰性非何杰金氏淋巴瘤，樣本極少 |
| [NCT03112174](https://clinicaltrials.gov/study/NCT03112174) | Phase 3 | 完成 | 366 | Ibrutinib＋venetoclax 對比 ibrutinib＋安慰劑，用於被套細胞淋巴瘤 |
| [NCT03984448](https://clinicaltrials.gov/study/NCT03984448) | Phase 2/3 | 進行中（不再招募） | 363 | Venetoclax＋化學免疫療法用於 MYC/BCL2 雙打擊淋巴瘤 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40009494](https://pubmed.ncbi.nlm.nih.gov/40009494/) | 2025 | RCT | Blood | MURANO 最終分析：venetoclax＋rituximab 用於復發／難治性 CLL，優於 bendamustine＋rituximab（疾病為 CLL，非本預測適應症） |
| [38700035](https://pubmed.ncbi.nlm.nih.gov/38700035/) | 2024 | Cohort | Am J Hematol | Polatuzumab＋venetoclax＋抗 CD20 用於復發／難治性 FL 與 DLBCL |
| [38264906](https://pubmed.ncbi.nlm.nih.gov/38264906/) | 2024 | Phase 1 | Leuk Lymphoma | Bendamustine、rituximab、ibrutinib、venetoclax 用於被套細胞淋巴瘤，常見血小板低下 |
| [28724540](https://pubmed.ncbi.nlm.nih.gov/28724540/) | 2017 | Review | Blood | 回顧 BCL-2 在 B 細胞淋巴瘤中的角色與 venetoclax |
| [35659041](https://pubmed.ncbi.nlm.nih.gov/35659041/) | 2022 | 文獻回顧 | J Hematol Oncol | 淋巴惡性腫瘤使用 venetoclax 的經驗，常見腫瘤溶解症候群與骨髓抑制 |
| [33775465](https://pubmed.ncbi.nlm.nih.gov/33775465/) | 2021 | 文獻回顧 | Blood Rev | Richter 轉化，少數情況為何杰金氏淋巴瘤 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65283 | VENCLEXTA TABLETS 50MG | — | 本報告彙整資料中未載明 |
| HK-65285 | VENCLEXTA TABLETS 100MG | — | 本報告彙整資料中未載明 |
| HK-65284 | VENCLEXTA TABLETS 10MG | — | 本報告彙整資料中未載明 |

三張皆為單一成分製劑，持有人為 ABBVIE LIMITED，狀態有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（BCL-2 抑制劑） |
| 骨髓抑制風險 | 文獻指出骨髓抑制與腫瘤溶解症候群為最常見的毒性 |
| 監測項目 | CBC（含分類）、腫瘤溶解相關電解質、肝腎功能 |

其餘項目請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下列出部分主要者：
  - 嚴重（Major）：Aprepitant、Dexamethasone、Clarithromycin、Eliglustat、Rolapitant、Fidaxomicin、Cobicistat、Deferiprone、Samarium (153Sm) lexidronam
  - 中度（Moderate）：Alvimopan、Loperamide、Cimetidine、Naldemedine、Metreleptin、Miconazole、Rifaximin、Clotrimazole、Troglitazone、Deferasirox
  - 輕微（Minor）：Naloxegol

警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 venetoclax 用於何杰金氏淋巴瘤，證據僅為 L5（模型預測）。
- 古典型何杰金氏淋巴瘤對 BCL-2 依賴較低，且現有淋巴瘤資料多為其他亞型。

**若要推進需要：**
- 何杰金氏淋巴瘤細胞 BCL-2 依賴性的前臨床或生物標記研究
- 何杰金氏淋巴瘤專屬的早期臨床試驗（Phase 1/2）
- 完整的作用機轉資料與香港仿單的警語、禁忌症
- 骨髓抑制與腫瘤溶解症候群的監測計畫，以及主要交互作用藥物（如 CYP3A 強抑制劑）的處置原則

---

**補充：本次資料中的其他預測適應症（供參考）**

| 預測適應症 | TxGNN 分數 | 證據概況 | 建議 |
|-----------|-----------|---------|------|
| 濾泡性淋巴瘤 | 0.9915 | 有多項 Phase 1/2 與 Phase 2 研究，無 Phase 3 | Proceed with Guardrails |
| 尤文氏肉瘤 | 0.9921 | 僅前臨床研究，無臨床試驗 | Hold |
| 轉移性腫瘤 | 0.9914 | 類別非特異，實體瘤證據限於 Phase 1、病例與前臨床 | 研究問題 |
| 惡性汗腺瘤 | 0.9912 | 無試驗與文獻 | Hold |

註：以上各適應症的證據等級為資料庫原始評分，未依本報告「須有直接研究該疾病」的上限規則重新核對，僅供參考。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

