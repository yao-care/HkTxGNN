---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eribulin：預測新適應症為纖維母細胞腫瘤 (Fibroblastic Neoplasm)（證據等級 L5）。原適應症：脂肪肉瘤"
monitor_inn: "ERIBULIN"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Eribulin：從脂肪肉瘤到纖維母細胞腫瘤

## 一句話總結

Eribulin 是一種微管動力學抑制劑，原本用於脂肪肉瘤治療。
TxGNN 模型的預測排名第一為**自體隱性家族性地中海熱**，但該預測完全沒有臨床證據支持。
本報告以證據最完整的**纖維母細胞腫瘤 (Fibroblastic Neoplasm)** 為主要評估對象，目前有 **1 個臨床試驗**和 **8 篇文獻**，其中多數為前臨床研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 脂肪肉瘤（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 纖維母細胞腫瘤 (Fibroblastic Neoplasm)（證據最完整的候選；預測排名第 1 者為自體隱性家族性地中海熱，分數 99.82%，無任何證據，建議 Hold） |
| TxGNN 預測分數 | 99.36%（纖維母細胞腫瘤）；排名第 1 的家族性地中海熱為 99.82% |
| 證據等級 | L2（此判定依據報告內的候選分級，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails（僅限纖維母細胞腫瘤／孤立性纖維性腫瘤方向的研究性推進） |

**說明：** 納入的 Phase 2 試驗人數少（16 人），結果數據未提供，嚴格依本報告的等級規則（需已完成的 Phase 2/3 RCT）可能偏高，保守看待應視為 L2 至 L4 之間。其餘 9 個預測中，7 個為 L5 或 L4 且皆為 Hold。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未提供 MOA）。根據已知資訊，Eribulin 是微管動力學抑制劑，屬於抗有絲分裂的細胞毒性藥物，已被證實可用於晚期脂肪肉瘤，並在其他軟組織肉瘤中顯示活性。

纖維母細胞腫瘤（包括孤立性纖維性腫瘤、纖維肉瘤）與脂肪肉瘤同屬軟組織肉瘤／間質腫瘤，在組織學類別上有關聯。已完成的 Phase 2 試驗 ERASING（NCT03840772）在晚期孤立性纖維性腫瘤中測試 Eribulin。前臨床研究也顯示 Eribulin 對纖維肉瘤細胞株（HT1080）有活性，並探討了抗藥性機制，以及與重組甲硫胺酸酶（rMETase）的協同作用。

需注意的限制：試驗規模小，結果未提供；前臨床資料僅為體外或異種移植模型；單臂設計為推測，資料中並未確認。

**其他預測新適應症（皆無直接證據）：**

| 預測疾病 | 分數 | 等級 | 備註 |
|---|---|---|---|
| 家族性地中海熱 | 99.82% | L5 | 與秋水仙素同為微管相關，但 Eribulin 毒性大（嗜中性白血球減少、神經病變），不適合長期用於自體發炎疾病 |
| 隆突性皮膚纖維肉瘤 | 99.66% | L4 | 僅有一般軟組織肉瘤化療綜述，主要以手術與 imatinib 治療 |
| 胸膜間皮瘤 | 99.51% | L5 | 抗有絲分裂藥物（如 vinorelbine）有部分活性，無 Eribulin 資料 |
| 惡性腹膜間皮瘤 | 99.47% | L5 | 同上，且罕見 |
| 卵巢黏液樣脂肪肉瘤 | 99.47% | L4 | 由已核准的脂肪肉瘤適應症外推，無部位特異性資料 |
| 胸膜腺瘤樣瘤 | 99.46% | L5 | 多為良性，不宜全身性化療 |
| 胸膜雙相型間皮瘤 | 99.37% | L5 | 肉瘤樣成分理論上可能有反應 |
| 胸膜上皮樣間皮瘤 | 99.35% | L5 | 僅為模型預測 |
| 心臟纖維肉瘤 | 99.35% | L4 | 極罕見，僅間接外推 |

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | 已完成 | 16 | ERASING 研究：Eribulin 用於晚期孤立性纖維性腫瘤；2019-07 開始，2024-09 完成；結果數據未提供 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | 腦膜外孤立性纖維性腫瘤的診斷與治療回顧 |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | 前臨床（異種移植） | Eur J Cancer | 病人來源的孤立性纖維性腫瘤異種移植模型顯示，trabectedin 或 Eribulin 可能有效 |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | 前臨床（體外） | Anticancer Res | rMETase 與 Eribulin 對纖維肉瘤細胞有顯著協同作用，對正常纖維母細胞則無 |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | 前臨床（體外） | Anticancer Res | rMETase 使高度抗藥的 HT1080 纖維肉瘤細胞對 Eribulin 的效力提高 16 倍 |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | 前臨床（體外／裸鼠） | In Vivo | 超抗藥的 HT1080 細胞惡性度更高，但 Eribulin 合併甲硫胺酸限制在裸鼠中有協同抑制效果 |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | 前臨床（細胞株建立） | Human Cell | 建立黏液纖維肉瘤細胞株 SMU-MFS，供新療法研發 |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | 前臨床（細胞株建立） | Human Cell | 建立黏液纖維肉瘤細胞株 NCC-MFS4-C1 |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | 病例報告 | Genes Chromosomes Cancer | 惡性周邊神經鞘瘤使用 entrectinib 的反應，與 Eribulin 無直接關係，相關性低 |

另有隆突性皮膚纖維肉瘤方向的綜述 [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/)（2016，Cancer，軟組織肉瘤化療），未提供 DFSP 特異性 Eribulin 數據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61632 | HALAVEN SOLUTION FOR INJECTION 0.88MG/2ML（Eisai） | 注射液 | 未提供 |
| HK-65349 | HALAVEN SOLUTION FOR INJECTION 0.88MG/2ML（Eisai） | 注射液 | 未提供 |
| HK-68262 | EBUNAT SOLUTION FOR INJECTION 0.88MG/2ML（I & C） | 注射液 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（微管動力學抑制劑） |
| 骨髓抑制風險 | 高（知識圖譜標示嗜中性白血球減少、血小板減少、顆粒球缺乏為風險） |
| 致吐性分級 | 低至中度（依藥物類別判斷，請參考仿單） |
| 監測項目 | CBC（含分類）、肝腎功能、電解質（鉀）、心電圖（QT） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜標示的風險疾病／狀況**（非仿單文字）：長 QT 症候群（含家族性）、血小板減少、低鉀血症、嗜中性白血球減少、顆粒球缺乏、周邊神經系統疾病與周邊神經病變、便祕。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 重大 (Major)：Dolasetron、Cisapride（皆與 QT 延長風險相關）。
  - 中等 (Moderate)：Ondansetron、Palonosetron、Clarithromycin、Levofloxacin、Metronidazole、Tinidazole、Famotidine、Loperamide、Rosuvastatin、Simvastatin，以及多種瀉劑（Bisacodyl、Lactulose、Lactitol、聚乙二醇、Picosulfuric acid、Sodium sulfate、Castor oil）。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**（僅限纖維母細胞腫瘤／孤立性纖維性腫瘤方向）

**理由：**
- 纖維母細胞腫瘤有 1 個已完成的 Phase 2 試驗，並有前臨床支持，且 Eribulin 在香港已上市、在脂肪肉瘤已有基礎。但試驗僅 16 人且結果未取得，證據仍有限。
- 其餘 9 個預測缺乏直接證據，皆維持 Hold。排名第 1 的家族性地中海熱在毒性與機轉上均不合理，不建議推進。

**若要推進需要：**
- 取得 NCT03840772（ERASING）的完整結果（反應率、無惡化存活期、安全性）。
- 補齊作用機轉資料與仿單警語、禁忌症（目前缺漏，屬阻擋性資料缺口）。
- 確認香港各許可證的核准適應症文字。
- 建立血液學、神經病變與 QT 間期的監測計畫，並審視與 QT 延長藥物的併用。
- 評估是否需要更大規模或對照的研究。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

