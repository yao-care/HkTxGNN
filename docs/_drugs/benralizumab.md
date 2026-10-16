---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benralizumab：預測新適應症為皮膚炎 (Dermatitis)（證據等級 L5）。原適應症：嗜酸性肺炎、肺嗜酸性球增多症"
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab：從嗜酸性肺炎到皮膚炎

## 一句話總結

Benralizumab 是一種抗 IL-5 受體 α 的單株抗體，原本用於嗜酸性肺炎與肺嗜酸性球增多症（知識圖譜所列適應症）。
TxGNN 模型預測它可能對**皮膚炎 (Dermatitis)** 有效，目前有 **3 個臨床試驗**和 **20 篇文獻**與此方向相關，但其中最大的第 2 期試驗（HILLIER）未顯示療效，證據並不樂觀。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 嗜酸性肺炎、肺嗜酸性球增多症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 皮膚炎 (Dermatitis) |
| TxGNN 預測分數 | 99.16% |
| 證據等級 | L5（已完成的 Phase 2 試驗未達 L1/L2 標準，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

**說明：** 預測排名第 1 的是免疫性血小板低下症（分數 99.34%），但完全沒有試驗或文獻支持，機轉上也缺乏關聯，因此本報告改以有實際研究資料的第 2 名「皮膚炎」為主軸。系統對皮膚炎給出的等級為 L2，但這項評級要求有一個已完成且具療效的 Phase 2/3 RCT；已完成的 HILLIER 研究是在 Phase 2 階段終止，且結果顯示無療效，因此本報告採較保守的判讀，並建議暫緩（Hold）。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未提供 MOA 欄位）。根據已知資訊，Benralizumab 靶向 IL-5 受體 α 亞基（IL5RA），可透過抗體依賴性細胞毒殺作用（ADCC）清除嗜酸性球與嗜鹼性球。它已在美國獲准用於嗜酸性氣喘，2024 年 9 月又擴大至嗜酸性肉芽腫併多發性血管炎（EGPA）。

嗜酸性肺炎與皮膚炎同屬第 2 型發炎相關疾病。在異位性皮膚炎中，嗜酸性球、嗜鹼性球與第 2 型innate lymphoid cells 參與皮膚發炎，因此從機轉上有一定合理性。

然而，這個合理性尚未得到臨床驗證。HILLIER 試驗顯示 benralizumab 對中重度異位性皮膚炎的症狀與體徵沒有效果，表示僅清除嗜酸性球可能不足以控制該疾病。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | 完成 | 20 | 探討 benralizumab 對異位性皮膚炎中嗜酸性球、嗜鹼性球與 ILC2 的影響；屬小型機轉研究，支持生物合理性但非決定性療效試驗 |
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | 終止 | 194 | HILLIER：隨機、雙盲、安慰劑對照，用於中重度異位性皮膚炎；已提前終止，發表結果顯示無療效 |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | 尚未招募 | 96 | 用於伴嗜酸性球增多與全身症狀的藥物反應（DRESS），預計 2027 年開始，尚無結果 |

---

## 文獻證據

資料中未提供隨機對照試驗（RCT）全文摘要，僅 HILLIER 結果有發表；其餘多為回顧性文章。以下依相關性列出代表性文獻（最多 10 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT | J Eur Acad Dermatol Venereol | HILLIER 試驗：benralizumab 對中重度異位性皮膚炎的症狀與體徵無效果 |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Review | J Allergy Clin Immunol Pract | 回顧包含 benralizumab 在內的 7 種生物製劑於異位性疾病孕期的安全性 |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie select | 更新異位性疾病、蕁麻疹與血管性水腫的生物製劑治療及過敏反應安全性 |
| [41297379](https://pubmed.ncbi.nlm.nih.gov/41297379/) | 2026 | Review | Respir Investig | 依氣喘共病（含異位性皮膚炎）選擇生物製劑 |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunol Allergy Clin North Am | 孕期與哺乳期使用單株抗體的資訊與知識缺口 |
| [32375958](https://pubmed.ncbi.nlm.nih.gov/32375958/) | 2020 | Review | Allergy Asthma Proc | 生物製劑用於口服類固醇依賴型氣喘 |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Review | Ann Allergy Asthma Immunol | 氣喘、蕁麻疹、異位性皮膚炎等的生物製劑選擇指引 |
| [33236428](https://pubmed.ncbi.nlm.nih.gov/33236428/) | 2020 | Review | Pediatr Allergy Immunol | 抗 IL-5 療法用於兒童過敏性疾病 |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy Asthma Proc | 免疫生物製劑用於重度氣喘、異位性皮膚炎與慢性蕁麻疹 |
| [37259416](https://pubmed.ncbi.nlm.nih.gov/37259416/) | 2023 | Review | Pharmaceuticals (Basel) | 氣喘與過敏疾病生物製劑的過去、現在與未來 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66015 | FASENRA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 30MG/1ML | 注射劑（預充填注射器） | 未載明 |
| HK-67113 | FASENRA SOLUTION FOR INJECTION IN PRE-FILLED PEN 30MG/1ML | 注射劑（預充填筆） | 未載明 |

兩張許可證均由 AstraZeneca Hong Kong Limited 持有，狀態皆為有效。

---

## 安全性考量

- **藥物交互作用**：目前僅有藥理標的資料，顯示其作用標的為 IL-5 受體 α 亞基（IL5RA），無具體藥物交互作用等級資料。

其餘主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 最相關的隨機對照 Phase 2 試驗（HILLIER，n=194）已終止，發表結果顯示 benralizumab 對異位性皮膚炎無效。其他預測適應症（免疫性血小板低下症、瘢痕疙瘩性痤瘡、皮肌炎）則完全沒有臨床證據，機轉上也無明確關聯。
- 僅憑高 TxGNN 分數不足以支持推進。

**若要推進需要：**
- 取得 HILLIER 完整結果與終止原因，釐清是否存在特定嗜酸性球高表現的亞群
- 評估較貼近機轉的嗜酸性球驅動皮膚疾病（如 DRESS，待 NCT06734884 結果）
- 取得香港仿單的警語、禁忌症與核准適應症，並補充作用機轉資料
- 在重新評估前，不建議針對皮膚炎投入進一步開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

