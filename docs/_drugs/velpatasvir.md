---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 929
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Velpatasvir：預測新適應症為B 型肝炎病毒感染 (Hepatitis B Virus Infection)（證據等級 L5）。原適應症：慢性 C 型肝炎病毒感染"
monitor_inn: "VELPATASVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever"]
---

# Velpatasvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Velpatasvir：從慢性 C 型肝炎到 B 型肝炎病毒感染
{: .text-alpha }

## 一句話總結

Velpatasvir 是 HCV NS5A 抑制劑，原本用於慢性 C 型肝炎病毒感染的治療。
TxGNN 模型預測它可能對 **B 型肝炎病毒感染 (Hepatitis B Virus Infection)** 有效，但目前有 **5 個臨床試驗**和 **20 篇文獻**與此方向相關，且這些資料都是 C 型肝炎研究，**沒有任何證據顯示它對 B 型肝炎本身有抗病毒效果**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染 |
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L3（僅有觀察性研究與綜述，且未直接支持 HBV 療效） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Velpatasvir 是 HCV NS5A 抑制劑，在 C 型肝炎中的療效已被證實（常與 sofosbuvir 合用，或與 sofosbuvir/voxilaprevir 三合一使用）。

然而，從機轉上看，這個預測並不穩固。HBV 是以逆轉錄方式複製的 DNA 病毒，沒有 NS5A 的同源蛋白，因此 Velpatasvir 沒有已知的直接抗 HBV 活性。TxGNN 的高分可能來自 B 型與 C 型肝炎同屬嗜肝性病毒疾病、在知識圖譜中彼此相近，而不是實際的藥理證據。

臨床上兩者的真正交集在於 **HBV/HCV 共感染**：以直接抗病毒藥物 (DAA) 治療 C 型肝炎時，可能誘發 B 型肝炎再活化，因此需要監測 HBV，並視情況預防性使用 TAF 等 HBV 藥物。這屬於安全性管理，不代表 Velpatasvir 本身能治療 B 型肝炎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | 中國 HCV/HBV 共感染患者，SOF/VEL 12 週併用預防性 TAF，目的是預防 HBV 再活化，而非評估 VEL 對 HBV 的活性 |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | 完成 | 803 | 緬甸簡化 HCV 檢測與治療示範計畫，無 HBV 療效指標 |
| [NCT07560046](https://clinicaltrials.gov/study/NCT07560046) | Phase 4 | 尚未招募 | 1280 | 重點族群 HCV 即時檢測與治療的群集隨機試驗，無 HBV 療效資料 |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | 未知 | 25 | HIV-HCV 共感染者的藥物轉換先導研究，HBV 活性來自 TAF，與 VEL 無關 |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | 完成 | 40 | HCV 相關惰性 B 細胞淋巴瘤使用 LDV/SOF 或 SOF/VEL，與 HBV 療效無關 |

---

## 文獻證據

下列為與 HBV 相關性較高的文獻（優先列出綜述與病例報告，其餘多為 HCV 療效研究）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | 慢性 C 型肝炎診斷與治療概述 |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | 兒童病毒性肝炎治療進展；HCV 有 DAA，HBV 目前仍無法治癒 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | DAA 治療失敗的 HCV 患者再治療 |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Review | AIDS Rev | 2017 年國際病毒性肝炎會議報告 |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | 使用 sofosbuvir/velpatasvir 治療 HCV 期間發生 HBV 再活化，與 HBsAg 免疫逃逸突變株有關 |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Cohort | Lancet Gastroenterol Hepatol | 盧安達 SOF/VEL 治療初治 HCV 的單臂試驗 |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort | Lancet Gastroenterol Hepatol | 盧安達 SOF/VEL/VOX 用於 DAA 失敗後再治療 |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | 未分類 | J Viral Hepat | 緬甸簡化 HCV 治療，HBV 共感染者同時接受 tenofovir |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | 未分類 | J Virus Erad | 中國真實世界 SOF/VEL 研究，含 HCV/HBV 共感染族群 |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | 未分類 | Klin Mikrobiol Infekc Lek | 捷克 Ostrava 兒童慢性 B 型與 C 型肝炎抗病毒治療回顧 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65046 | EPCLUSA TABLETS 400MG/100MG | 錠劑 | 請參考原廠仿單 |
| HK-65775 | VOSEVI TABLETS | 錠劑 | 請參考原廠仿單 |

兩張許可證均由 Gilead Sciences Hong Kong Limited 持有，狀態皆為有效。

---

## 安全性考量

- **藥物交互作用**：共查詢到 57 筆交互作用，主要如下：
  - **重大 (Major)**：dexamethasone，以及多種氫離子幫浦抑制劑（omeprazole、esomeprazole、lansoprazole、dexlansoprazole、pantoprazole、rabeprazole）
  - **中度 (Moderate)**：制酸劑（氫氧化鋁、碳酸鈣、氫氧化鎂、氧化鎂、碳酸鎂、magaldrate）、H2 受體阻斷劑（cimetidine、famotidine、nizatidine）、naldemedine
  - **輕微 (Minor)**：fidaxomicin、naloxegol、prucalopride
- **HBV 再活化風險**：文獻病例報告顯示，HCV 患者接受 DAA 治療期間可能發生 B 型肝炎再活化，共感染或 HBcAb 陽性者需監測 HBV，並評估是否預防性使用 TAF 等 HBV 藥物。

警語與禁忌症的仿單內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Velpatasvir 是 HCV NS5A 抑制劑，HBV 沒有對應的作用標的，所有相關試驗與文獻都是 HCV 研究，沒有 HBV 療效證據。TxGNN 高分較可能來自知識圖譜中肝炎病毒疾病的網路相近性。
- 此預測目前只能視為研究假說。真正有臨床意義的是 HCV/HBV 共感染時的再活化監測與預防。

**若要推進需要：**
- 補充 Velpatasvir 作用機轉資料
- 體外試驗確認 Velpatasvir 是否對 HBV 複製有任何抑制活性
- 若體外有訊號，再設計 HBV 感染的早期臨床研究
- 針對 HCV/HBV 共感染族群，建立 HBV 再活化的監測與預防流程（例如搭配 TAF）
- 取得香港仿單，確認警語與禁忌症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

