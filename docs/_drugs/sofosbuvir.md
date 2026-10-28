---
layout: default
title: Sofosbuvir
parent: 高證據等級 (L1-L2)
nav_order: 825
evidence_level: L2
indication_count: 8
monitor_inn: "SOFOSBUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "chronic hepatitis B virus infection", "Kyasanur forest disease", "HIV infectious disease"]
last_modified_at: 2026-10-28
description: "Sofosbuvir：預測新適應症為B 型肝炎病毒感染（證據等級 L5）。原適應症：慢性 C 型肝炎病毒感染"
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L2** | 預測適應症: **8** 個
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

## Sofosbuvir：從 C 型肝炎到 B 型肝炎病毒感染
{: .text-alpha }

## 一句話總結

Sofosbuvir（索非布韋）是一種核苷酸類似物抗病毒藥，知識圖譜中記錄的原適應症為慢性 C 型肝炎病毒感染。
TxGNN 模型排名第一的預測是 **B 型肝炎病毒感染 (Hepatitis B Virus Infection)**，但機轉與臨床資料都不支持其具抗 B 肝療效；機轉與直接證據較合理的方向是 **E 型肝炎病毒感染 (Hepatitis E Virus Infection)**（1 個 Phase 2 試驗與多篇文獻）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染（知識圖譜中記錄的關係；本地許可證資料未載明適應症文字） |
| 預測新適應症 | B 型肝炎病毒感染（排名第一）；E 型肝炎病毒感染（機轉與證據較合理，另行說明） |
| TxGNN 預測分數 | 0.9977（B 型肝炎）；0.9949（E 型肝炎） |
| 證據等級 | B 型肝炎：L2；E 型肝炎：L2 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | B 型肝炎：Hold（列為研究問題）；E 型肝炎：Proceed with Guardrails |

> 註：本報告依預測排名以 B 型肝炎為主要預測，但因其證據多屬 C/B 型共感染情境，下文亦並列 E 型肝炎以供比較。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉登錄資料。依已知藥理，Sofosbuvir 是 HCV NS5B RNA 依賴性 RNA 聚合酶 (RdRp) 的核苷酸類似物抑制劑，活性三磷酸代謝物可終止病毒 RNA 合成。

**B 型肝炎：** HBV 是 DNA 病毒，經反轉錄酶複製，與 NS5B 沒有直接的標靶對應，因此 TxGNN 的高分並未獲得機轉支持。現有試驗多為 HCV/HBV 共感染，重點在 C 肝治癒及 B 肝再活化的監測，而非 B 肝療效。一項 Phase 2 開放標籤研究（ledipasvir/sofosbuvir 用於 HBV 感染者）觀察到 HBsAg 有限度下降，但規模小且為單臂。

**E 型肝炎：** HEV 為正股 RNA 病毒，具 RdRp，Sofosbuvir 的作用機轉有合理性。體外研究顯示可抑制 HEV 複製，與 ribavirin 併用有相加效果。然而臨床療效有限：Phase 2 前導試驗顯示病毒量初期下降但未達持續病毒學反應，並出現抗藥相關變異。

---

## 臨床試驗證據

### B 型肝炎（排名第一的預測）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | 完成 | 21 | ledipasvir/sofosbuvir 12 週用於 HBV 感染者，單臂小型研究 |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | HCV/HBV 共感染接受 DAA 治療，監測 HBV 再活化 |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Phase 3 | 完成 | 72 | 隨機開放標籤，比較固定複方與 sofosbuvir+daclatasvir（基因型 4 HCV），主要終點為 HCV |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | SOF/VEL 合併預防性 TAF 用於 HCV/HBV 共感染；B 肝保護來自 TAF |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | 未知 | 21 | ledipasvir/sofosbuvir 用於 HCV 相關惰性 B 細胞淋巴瘤 |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | 未知 | 25 | HIV-HCV 共感染轉換治療；B 肝活性來自含 TAF 方案 |

### E 型肝炎

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03282474](https://clinicaltrials.gov/study/NCT03282474) | Phase 2 | 完成 | 10 | HepNet 前導試驗，sofosbuvir 治療慢性 E 型肝炎；效果短暫、未持續 |

---

## 文獻證據

### B 型肝炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 開放標籤試驗 | J Med Virol | LDV/SOF 用於 HBV 單一感染，以 HBsAg 與 HBV DNA 下降為終點 |
| [42558970](https://pubmed.ncbi.nlm.nih.gov/42558970/) | 2026 | 臨床研究 | J Clin Transl Hepatol | SOF/VEL 搭配 TAF 前處理於 HBV/HCV 共感染的安全性與 HBV 再活化 |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | 世代研究 | J Clin Med | HCV 共感染者接受 DAA 期間 HBV-DNA 與 HBsAg 動力學不同 |
| [26967675](https://pubmed.ncbi.nlm.nih.gov/26967675/) | 2016 | 文獻回顧 | J Clin Virol | DAA 治療 HCV 時 HBV 再活化的挑戰 |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | 藥物不良反應報告 | Hosp Pharm | simeprevir 與 sofosbuvir 治療 HCV 時發生 HBV 再活化 |

### E 型肝炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35814503](https://pubmed.ncbi.nlm.nih.gov/35814503/) | 2022 | Review | J Clin Exp Hepatol | 回顧 sofosbuvir 治療 HEV 的體外與體內證據 |
| [26408347](https://pubmed.ncbi.nlm.nih.gov/26408347/) | 2016 | 體外研究 | Gastroenterology | sofosbuvir 抑制 HEV 基因型 3 複製，與 ribavirin 相加 |
| [35247472](https://pubmed.ncbi.nlm.nih.gov/35247472/) | 2022 | 動物研究 | Antiviral Res | 高劑量 sofosbuvir 及與 ribavirin 併用抑制兔 HEV 複製 |
| [37334496](https://pubmed.ncbi.nlm.nih.gov/37334496/) | 2023 | 臨床試驗分析 | Hepatology | 治療期間出現抗藥相關變異，無持續病毒學反應 |
| [31404927](https://pubmed.ncbi.nlm.nih.gov/31404927/) | 2019 | 病例系列 | Open Forum Infect Dis | 3 名器官移植受者加用 sofosbuvir 未能清除 HEV |
| [36942308](https://pubmed.ncbi.nlm.nih.gov/36942308/) | 2023 | 病例報告 | IDCases | ribavirin 難治性 HEV 對 LDV/SOF 加 ribavirin 有反應 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65046 | EPCLUSA TABLETS 400MG/100MG | 未載明 | 未載明 |
| HK-65775 | VOSEVI TABLETS | 未載明 | 未載明 |

> 以上兩張許可證的品名顯示為複方製劑（含 sofosbuvir 與其他成分），其資訊不代表單方 sofosbuvir 的核准或上市情形。

---

## 安全性考量

- **藥物交互作用**（共 8 項紀錄，以下列出主要者）：
  - 嚴重 (Major)：Apalutamide、Enzalutamide、Lorlatinib
  - 中度 (Moderate)：Fostamatinib、Warfarin、Dicoumarol、Encorafenib
  - 輕度 (Minor)：Cyclosporine
- **B 型肝炎再活化**：多篇文獻（含病例報告與前瞻性研究）顯示，HCV/HBV 共感染者接受含 sofosbuvir 的 DAA 治療時可能發生 HBV 再活化，需在治療前篩檢並考慮預防性抗 HBV 治療。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：**
- **B 型肝炎：Hold（列為研究問題）**
- **E 型肝炎：Proceed with Guardrails**

**理由：**
- B 型肝炎：雖然 TxGNN 分數最高（0.9977），但 sofosbuvir 針對 HCV NS5B，與 HBV 無直接機轉對應。現有證據大多是共感染背景下的 B 肝再活化安全議題，而非療效。證據等級依有直接研究的 Phase 2 試驗評為 L2，但其強度有限（單臂、小樣本）。
- E 型肝炎：有機轉合理性、體外與動物資料，以及 1 個直接的 Phase 2 前導試驗，但療效短暫且有抗藥變異，故僅適合在嚴格條件下探索。

**若要推進需要：**
- B 型肝炎：設計 HBV 單一感染的對照試驗，驗證 HBsAg／HBV DNA 的持續下降；同時建立 DAA 治療期間的 HBV 再活化篩檢與預防流程。
- E 型肝炎：較大規模、含對照的試驗，探討劑量（可能需高劑量）、與 ribavirin 併用及抗藥性監測。
- 補齊作用機轉與香港仿單的警語、禁忌症資料。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

