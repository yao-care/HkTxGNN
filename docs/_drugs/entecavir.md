---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entecavir：預測新適應症為慢性 C 型肝炎 (Chronic hepatitis C virus infection)（證據等級 L5）。原適應症：慢性 B 型肝炎病毒感染"
monitor_inn: "ENTECAVIR"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
---

# Entecavir
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

# Entecavir：從慢性 B 型肝炎到慢性 C 型肝炎

## 一句話總結

Entecavir 是一種核苷類似物抗病毒藥，原本用於治療慢性 B 型肝炎病毒感染。
TxGNN 模型預測它可能對**慢性 C 型肝炎 (Chronic hepatitis C virus infection)** 有效，
但目前僅有 **2 個間接相關的臨床試驗**和 **20 篇文獻**，且這些資料談的都是 B 型肝炎成分，並非 C 型肝炎本身的療效，因此這個預測的實質證據很弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎病毒感染（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 慢性 C 型肝炎 (Chronic hepatitis C virus infection) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L4（僅有間接的機轉與共感染研究，無 C 型肝炎本身的療效證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。依已知藥理，Entecavir 是鳥苷核苷類似物，在體內轉為活性三磷酸形式後，抑制 B 型肝炎病毒 (HBV) 聚合酶，也就是病毒的引發、反轉錄與 DNA 合成。

C 型肝炎病毒 (HCV) 是 RNA 病毒，靠 NS5B RNA 依賴性 RNA 聚合酶複製。Entecavir 並不作用於這個酶，**機轉上沒有合理的直接抗 HCV 作用**。TxGNN 的高分較可能反映的是 B 型與 C 型肝炎在疾病網絡上的相近，而不是藥物對 HCV 真的有效。

相關臨床研究都是 HBV/HCV 共感染的情境：HCV 由直接作用抗病毒藥 (DAA) 治療，Entecavir 的角色是預防 HBV 在 DAA 治療期間再活化。這是 B 型肝炎的管理，不是治療 C 型肝炎。而且 HCV 現在已可用 DAA 治癒，重新定位 Entecavir 並無臨床必要。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | HCV/HBV 共感染患者接受 DAA 期間，評估 HBV 再活化的發生率與相關因素；HCV 活性藥物是 DAA，非 Entecavir |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | 無分期 | 未知 | 60 | 隨機三組試驗，比較在 DAA 治療時預防性使用核苷類似物（12 週 vs 24 週）能否預防 HBV 再活化；針對 HBV，非 HCV |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | HBV/HCV 共感染風險高，需有效治療 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | 回顧 B 型、C 型肝炎抗病毒藥（含 Entecavir）及其對腎功能的影響 |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | 慢性病毒性肝炎治療；B 型肝炎以核苷（酸）類似物長期抑制病毒 |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | 66 位抗 HCV 抗體陽性的慢性 B 型肝炎患者，觀察接受抗 HBV 治療後 HCV 再活化情形 |
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | RCT（依標題判斷） | Clin Gastroenterol Hepatol | Entecavir 可預防 HCV/HBV 雙重感染者在 DAA 治療期間的 HBV 再活化 |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | 未分類 | Dig Dis | 探討接受 DAA 治療 C 型肝炎者的 HBV 再活化發生率與臨床過程 |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | 未分類 | J Gastroenterol Hepatol | 探討慢性 C 型肝炎合併 HBV 感染者使用 DAA 時的 HBV 再活化風險 |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | 未分類 | World J Hepatol | 肝、腎移植前後 B、C 型肝炎處置；Entecavir、Tenofovir 可預防移植後 HBV 復發 |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | 未分類 | Clin Res Hepatol Gastroenterol | 兒童 B 型與 C 型肝炎的現在與未來處置 |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | 未分類 | Best Pract Res Clin Gastroenterol | 慢性病毒性肝炎纖維化；HBV 病毒抑制可改善發炎與纖維化 |

---

## 香港上市資訊

Entecavir 在香港共有 20 張有效單一成分許可證，以下列出 5 張主要許可證（資料中未載明劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55152 | BARACLUDE TAB 0.5MG（Bristol-Myers Squibb） | 錠劑 | 未載明 |
| HK-55153 | BARACLUDE TAB 1MG（Bristol-Myers Squibb） | 錠劑 | 未載明 |
| HK-65737 | ENTECAVIR LEK SANDOZ TABLETS 0.5MG（Sandoz） | 錠劑 | 未載明 |
| HK-68822 | ENTECAVIR TEVA TABLETS 0.5MG（Teva） | 錠劑 | 未載明 |
| HK-64435 | PMS-ENTECAVIR TABLETS 0.5MG（Trenton-Boma） | 錠劑 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎情況**（來自藥物－疾病關聯，非仿單原文）：腎功能不全、脂肪肝、非酒精性脂肪肝炎、乳酸中毒。
- **藥物交互作用**：共查得 44 筆，以下為中度交互作用的主要例子：
  - 腎毒性或影響腎排泄的藥物：Amphotericin B（含脂質體等劑型）、Vancomycin、Kanamycin、Neomycin、Polymyxin B
  - 胃酸抑制劑：Famotidine、Ranitidine、Cimetidine
  - 其他：Metformin、Amoxicillin、Levofloxacin、Mesalazine、Sulfasalazine、Orlistat
- 文獻另提到，核苷類似物有類別性不良反應（肌病、神經病變、乳酸中毒），並有 Entecavir 相關血小板低下的個案報告。

完整警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Entecavir 作用於 HBV 聚合酶，對 HCV 的 NS5B 聚合酶沒有已知作用，所有相關試驗與文獻討論的都是 B 型肝炎成分，並非 HCV 療效。C 型肝炎已有高治癒率的 DAA，沒有重新定位的臨床必要。
- TxGNN 分數很高，但更可能反映疾病網絡的相近性。

**若要推進需要：**
- 先有體外 HCV 複製子等基礎實驗，證明對 HCV 有直接活性。
- 取得完整作用機轉資料與香港仿單的警語、禁忌資料（目前缺乏）。
- 臨床上的實際價值在於 HCV/HBV 共感染者 DAA 治療期間的 HBV 再活化預防，這屬於原適應症的延伸應用，不是新適應症。

---

**補充：其他預測適應症的排序**

- **B 型肝炎病毒感染（排名 2）**：這是已核准的原適應症，並非新的重新定位對象。有多項已完成的 Phase 3 試驗（如 NCT00395018、NCT00410072、NCT01063036）及 EASL 2017 指引支持，證據等級 L1，建議為 Proceed with Guardrails，可作為陽性對照。
- **HIV 感染（排名 3）**：證據等級 L3。Entecavir 對 HIV-1 僅有微弱活性，且會選出 M184V 突變，可能損害 HIV 治療選擇；試驗的終點是 HBV 病毒血症，並非 HIV 控制。不建議作為 HIV 治療，僅適合在完全抑制性抗反轉錄病毒療法下用於 HBV 共感染。
- **其餘預測**（C 型肝炎病毒感染、E 型肝炎、A 型肝炎、動物病毒性肝炎、猿猴免疫缺乏病毒、貓後天免疫缺乏症候群、罕見神經發展疾病）：缺乏合理機轉或僅為模型預測，皆為 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

