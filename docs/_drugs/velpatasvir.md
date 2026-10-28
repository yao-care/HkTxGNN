---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 929
evidence_level: L5
indication_count: 10
monitor_inn: "VELPATASVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Velpatasvir：預測新適應症為B 型肝炎病毒感染（證據等級 L5）。原適應症：慢性 C 型肝炎"
---

# Velpatasvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Velpatasvir：從 C 型肝炎到 B 型肝炎病毒感染
{: .text-alpha }

## 一句話總結

Velpatasvir 是 C 型肝炎病毒 (HCV) NS5A 抑制劑，知識圖譜中記錄的原適應症為慢性 C 型肝炎。
TxGNN 模型預測它可能對**B 型肝炎病毒感染 (Hepatitis B Virus Infection)** 有效，但本報告所整理的資料中，沒有任何研究直接驗證 velpatasvir 對 B 型肝炎的療效，因此證據等級僅為 **L5（僅模型預測）**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎（知識圖譜記錄；本地許可證資料未載明適應症文字） |
| 預測新適應症 | B 型肝炎病毒感染 |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 velpatasvir 是 HCV NS5A 抑制劑，用於 C 型肝炎。

B 型肝炎病毒是 DNA 病毒，靠逆轉錄酶／聚合酶複製，與 HCV 的複製機制不同，也沒有 NS5A 對應標靶。因此從機轉上看，velpatasvir 對 HBV 並無已知的抗病毒活性。此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性（例如兩者同為嗜肝病毒），並非生物學證據。

臨床上與 HBV 相關的主要情境是 HCV/HBV 共感染：HCV 直接抗病毒藥物治療可能誘發 HBV 再活化。因此現有資料涉及的是安全性與監測，而非抗 HBV 療效。

## 臨床試驗證據

以下試驗均未直接以 velpatasvir 治療 B 型肝炎為研究主題。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | HCV/HBV 共感染患者使用 12 週 SOF/VEL 併用預防性 TAF；抗 HBV 作用來自 TAF，而非 velpatasvir |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | 未知 | 25 | HIV/HCV 共感染者的 SOF/VEL 治療與抗反轉錄病毒藥物轉換可行性，與 HBV 僅間接相關 |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | 完成 | 803 | 緬甸簡化 HCV 檢測與治療模式，無 HBV 療效終點 |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | 完成 | 40 | HCV 相關惰性 B 細胞淋巴瘤的無干擾素治療，與 HBV 無關 |
| [NCT07560046](https://clinicaltrials.gov/study/NCT07560046) | Phase 4 | 尚未招募 | 1280 | HCV 即時檢測與治療的叢集隨機試驗，無 HBV 終點 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | HBV 核心抗體陽性患者在 SOF/VEL 治療期間發生 HBV 再活化，與表面抗原免疫逃脫突變株相關 |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | 世代研究 | J Viral Hepat | 緬甸簡化 HCV 治療策略；合併 HBV 者同時使用 tenofovir |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | 真實世界研究 | J Virus Erad | 中國患者 SOF/VEL 的療效與安全，含 HCV/HBV 共感染族群 |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | 回顧 | World J Gastroenterol | 兒童病毒性肝炎治療進展，提及 HBV 治療仍遠未達治癒 |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | 慢性 C 型肝炎診斷與治療概述 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65046 | EPCLUSA TABLETS 400MG/100MG | 未載明 | 未載明 |
| HK-65775 | VOSEVI TABLETS | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 57 項交互作用。
  - 嚴重（Major）：dexamethasone，以及多種氫離子幫浦抑制劑（omeprazole、esomeprazole、lansoprazole、dexlansoprazole、pantoprazole、rabeprazole）。
  - 中度（Moderate）：制酸劑（氫氧化鋁、碳酸鈣、氫氧化鎂、氧化鎂等）與 H2 受體阻斷劑（cimetidine、famotidine、nizatidine）。
- **HBV 再活化風險**：文獻顯示 HCV 直接抗病毒藥物治療期間，HBV 感染者可能發生 HBV 再活化，使用前須評估 HBV 狀態。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有研究證實 velpatasvir 對 B 型肝炎有療效，機轉上也缺乏合理連結，高預測分數可能只反映網路鄰近性。
- 現有相關證據僅涉及 HCV/HBV 共感染的安全性與 HBV 再活化監測，而非新適應症。

**若要推進需要：**
- 體外試驗確認 velpatasvir 是否具抗 HBV 活性
- 取得香港仿單的警語、禁忌症與適應症文字
- 補充 velpatasvir 的作用機轉資料
- 若關注共感染族群，應另行設計 HBV 再活化預防與監測策略，而非視為抗 HBV 適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

