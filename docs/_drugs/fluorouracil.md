---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil：從癌症化療到陰道葡萄狀胚胎型橫紋肌肉瘤

## 一句話總結

Fluorouracil（5-FU）是氟嘧啶類細胞毒性抗代謝物，廣泛用於大腸直腸癌、乳癌、胃癌等惡性腫瘤的化療方案中。
TxGNN 模型將其頂排預測至**陰道葡萄狀胚胎型橫紋肌肉瘤 (botryoid-type embryonal rhabdomyosarcoma of the vagina)**，然而此適應症目前**無任何臨床試驗或文獻支持**；整體 10 項預測中，僅肝肉瘤（Rank 7）具備中等間接證據（L3），其餘 9 項均建議 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港無上市許可（普遍用於消化道腫瘤等化療） |
| 預測新適應症 | 陰道葡萄狀胚胎型橫紋肌肉瘤 (Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5（頂排適應症）；L3（肝肉瘤 Rank 7，為最佳次選） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 Evidence Pack 缺乏正式的作用機轉（MOA）資料。根據已知藥理學，5-FU 是氟嘧啶類抗代謝物，主要透過抑制胸腺嘧啶合成酶（thymidylate synthase, TS）阻礙 DNA 合成，以及將異常氟化核苷酸摻入 RNA，從而殺傷快速分裂的腫瘤細胞。

橫紋肌肉瘤（Rhabdomyosarcoma, RMS）為高度惡性的軟組織肉瘤，細胞增殖旺盛，理論上 5-FU 的廣譜抗增殖機轉存在跨腫瘤類別活性的可能性。然而，**現代 RMS 標準化療方案為 VAC（長春新鹼 + 放射菌素 D + 環磷醯胺）或 IVA 方案，並未納入 5-FU**，且現有文獻均無直接在 RMS 使用 5-FU 的臨床設計。

TxGNN 對頂排 6 項 RMS 亞型的高預測分數（均 > 99.7%），極可能源自知識圖譜中「化療藥物節點 ↔ 肉瘤節點」的拓撲鄰近性，而非反映直接臨床效力。頂排適應症（陰道葡萄狀 RMS）另有解剖位置的特殊考量，5-FU 在此亞型毫無已發表的臨床資料。

---

## 臨床試驗證據

**頂排適應症（陰道葡萄狀胚胎型橫紋肌肉瘤）**

目前無相關臨床試驗登記。

---

**補充：肝肉瘤（Rank 7，本報告最佳證據適應症）**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03914170](https://clinicaltrials.gov/study/NCT03914170) | N/A | 完成 | 70 | 回顧性評估含 5-FU 的 FOLFIRINOX 三聯療法用於 RAS 野生型轉移性大腸直腸癌，按 BRAF 狀態及腫瘤原發位置分層分析療效 |
| [NCT01374425](https://clinicaltrials.gov/study/NCT01374425) | Phase 2 | 完成 | 376 | Bevacizumab + mFOLFOX6 vs FOLFIRI 用於未治療轉移性大腸直腸癌，評估化療生物標記與 PFS 之關聯性 |
| [NCT01228734](https://clinicaltrials.gov/study/NCT01228734) | Phase 3 | 完成 | 553 | Cetuximab + FOLFOX-4 vs FOLFOX-4 治療 RAS 野生型轉移性大腸直腸癌（中國受試者），評估 PFS 與生物標記 |
| [NCT04999761](https://clinicaltrials.gov/study/NCT04999761) | Phase 1 | 招募中 | 917 | AB122（PD-1/LAG-3 雙抗）用於廣義固態瘤安全性平台研究，理論上可納入肝肉瘤，非針對性 |
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | Phase 4 | 招募中 | 40 | Atezolizumab + Bevacizumab 合併 Y90 放射栓塞治療肝細胞癌橋接移植或降期，不含 5-FU，僅作背景參考 |

> ⚠️ 以上試驗均以大腸直腸癌為適應症，並非直接針對肝肉瘤；5-FU 方案安全性數據可間接參考，但不構成肝肉瘤的直接臨床支持。

---

## 文獻證據

**頂排適應症（陰道葡萄狀胚胎型橫紋肌肉瘤）**

目前無相關文獻。

---

**補充：肝肉瘤（Rank 7，本報告最佳證據適應症）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [29346784](https://pubmed.ncbi.nlm.nih.gov/29346784/) | 2019 | 回顧性病例系列 | Digestive Surgery | 中國單一中心分析原發性肝肉瘤（PLS）的臨床特徵、手術切除及術後化療預後 |
| [37112602](https://pubmed.ncbi.nlm.nih.gov/37112602/) | 2023 | 前臨床/實驗 | Toxics | 5-FU 聯合洋甘菊提取物治療 Sarcoma 180 移植小鼠，評估腫瘤抑制率與毒性組合效果 |
| [52569](https://pubmed.ncbi.nlm.nih.gov/52569/) | 1975 | 動物研究 | Gan | 比較絲裂黴素 C、博來黴素、環磷醯胺、5-FU 等多種藥物對肝/腎/肺 Sarcoma 180 小鼠存活時間的影響 |
| [10584572](https://pubmed.ncbi.nlm.nih.gov/10584572/) | 1999 | 前臨床 | Gan to Kagaku Ryoho | HCFU（5-FU 前驅藥）聯合 TNP-470 抗血管生成劑對 BALB/c 腹膜後肉瘤肝轉移模型的療效 |
| [3603715](https://pubmed.ncbi.nlm.nih.gov/3603715/) | 1987 | 回顧性多中心 | Tumori | 義大利多中心回顧 8 例未滿 19 歲肝未分化肉瘤的臨床特徵與治療結果 |
| [11294295](https://pubmed.ncbi.nlm.nih.gov/11294295/) | 2001 | 病例報告 | J Hepatobiliary Pancreat Surg | 2 例兒童破裂性肝未分化肉瘤，採 CDDP/ADR/CPM 方案治療，報告手術時機與化療反應 |
| [1406088](https://pubmed.ncbi.nlm.nih.gov/1406088/) | 1992 | 藥物動力學 | Magn Reson Imaging | 19F MRS 研究胸腺嘧啶調節劑對肝臟及 RIF-1 纖維肉瘤腫瘤中 5-FU 代謝動力學的影響 |
| [12918123](https://pubmed.ncbi.nlm.nih.gov/12918123/) | 2003 | 動物研究 | World J Gastroenterol | 5-FU 緩釋植入劑對 Walker 256 carcinosarcoma Wistar 大鼠的毒性分布及抗腫瘤效果 |
| [9873095](https://pubmed.ncbi.nlm.nih.gov/9873095/) | 1999 | 綜述 | Liver Transplant Surg | 肝臟轉移病變處置綜述，含大腸直腸癌與胃腸肉瘤肝轉移之化療選項（5-FU 為主要方案之一） |
| [28239866](https://pubmed.ncbi.nlm.nih.gov/28239866/) | 2017 | 藥動學/動物 | Biopharm Drug Dispos | 血管調節劑（腎上腺素/肼苯達嗪）對大鼠肝臟表面局部給予 5-FU 後腫瘤模型中藥物分佈的影響 |

---

## 細胞毒性

Fluorouracil 為氟嘧啶類抗腫瘤藥物，屬傳統細胞毒性藥物，須列示以下安全資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類／抗代謝物） |
| 骨髓抑制風險 | 中至高度（常見嗜中性白血球減少、血小板減少、貧血，高劑量或長期輸注風險更高） |
| 致吐性分級 | 低至中度（靜脈推注 > 持續輸注；聯合方案致吐性依組合藥物決定） |
| 監測項目 | CBC 含白血球分類計數、肝功能（ALT/AST）、腎功能（BUN/Cr）、電解質、黏膜炎評估 |
| 處置防護 | 依細胞毒性藥物調配規範操作；需配戴雙層防護手套，於生物安全操作臺調配，避免皮膚與黏膜接觸 |

> 本 Evidence Pack 之安全性資訊為 Data Gap，詳細骨髓毒性及禁忌事項請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **機轉安全警示（Rank 8–10）**：預測清單末三項為鐮刀型細胞貧血症及地中海貧血合併症。5-FU 骨髓抑制作用對已存在慢性貧血的此類患者可能誘發再生不良危機（aplastic crisis），機轉上明顯不適宜，應**直接排除，不進行後續評估**。

---

## 結論與下一步

**決策：Hold**

**理由：**
頂排 6 項預測（各 RMS 亞型）在知識圖譜層面具生物學合理性，但 5-FU 不屬於 RMS 現行任何標準化療方案，且全部缺乏直接臨床試驗與文獻支持（均為 L5）。Rank 7（肝肉瘤）雖具間接文獻支撐（L3），但 5 項相關試驗均針對大腸直腸癌，直接人體證據不足以進入決策評估階段。Rank 8–10 有明確安全性疑慮，排除。整體評估在取得基礎安全性與 MOA 資料前，尚無條件推進。

**若要推進需要：**
- **補齊仿單安全性資料**（Blocking Data Gap）：下載原廠仿單 PDF 解析警語與禁忌症，否則無法進行 S1 安全性初評
- **補齊 MOA 資料**：透過 DrugBank API 確認 5-FU 與 RMS / 肝肉瘤的機轉關聯性
- **聚焦肝肉瘤文獻深度盤查**：區分「原發性肝肉瘤（PLS）」與「消化道癌肝轉移」的 5-FU 相關文獻，確認真正相關的直接人體數據
- **鐮刀型細胞疾病（Rank 8–10）直接排除**：機轉矛盾，不建議任何後續評估
- 若後續評估聚焦肝肉瘤，建議與肝臟腫瘤外科及血液腫瘤科共同設計 Pilot 研究方案
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

