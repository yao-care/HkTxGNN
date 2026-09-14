---
layout: default
title: Sodium Tetradecyl Sulfate
parent: 高證據等級 (L1-L2)
nav_order: 696
evidence_level: L1
indication_count: 10
---

# Sodium Tetradecyl Sulfate
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Sodium Tetradecyl Sulfate：從靜脈硬化劑到食道靜脈曲張（無出血）預防性治療

## 一句話總結

Sodium tetradecyl sulfate（STS）是一種血管內硬化劑，原始核准適應症資料在本次 Evidence Pack 中缺失，但依國際上已知用途主要用於周邊靜脈曲張的硬化治療。TxGNN 模型預測它可能對**食道靜脈曲張（無出血）(Esophageal Varices without Bleeding)** 有效，目前有 **8 篇具明確分類的高品質文獻**（含 4 篇 RCT）支持這個方向，但**臨床試驗登記為 0 筆**。

> ⚠️ 補充說明：本 Evidence Pack 中的文獻顯示，STS 早在 1987–1998 年間就已有多項 RCT 直接用於食道／胃靜脈曲張出血的急性期硬化治療（見 rank 2「有出血」項目），顯示此「預測適應症」實際上更接近**已存在數十年的臨床慣例**，而非全新機轉假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（Evidence Pack 未提供核准適應症；本藥品於香港未上市，無許可證資料） |
| 預測新適應症 | 食道靜脈曲張（無出血）Esophageal Varices without Bleeding |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料（Data Gap，DG002）。根據 Evidence Pack 提供的文獻內容可推知，STS 屬於**血管內硬化劑（sclerosing agent）**，其藥理作用是使血管內皮受損、誘發血栓形成與纖維化，達到閉塞異常血管的效果。

食道靜脈曲張是門脈高壓症患者常見的血管病灶，其治療原理與周邊靜脈曲張硬化治療高度相似——都是利用 STS 對血管內皮的化學損傷作用達到血管閉塞目的。事實上，Evidence Pack 中收錄的多篇 1987–1998 年 RCT（如 pmid 8886633、1734694、8287811、2279644）已直接證實 STS 用於食道／胃靜脈曲張硬化治療的療效，與其他硬化劑（polidocanol、ethanolamine oleate、sodium morrhuate）相當。

因此本預測的機轉合理性相對明確：**這不是全新的機轉外推，而是模型從知識圖譜結構中重新發現了一個已被臨床實務長期採用、但可能未被正式收錄於現行適應症清單的用途。**

---

## 臨床試驗證據

目前無相關臨床試驗登記（predicted_indications 排名第 1 之「食道靜脈曲張（無出血）」項目）。

> 補充：知識圖譜中緊鄰的「食道靜脈曲張（有出血）」適應症有 1 筆登記試驗：
> [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) — Phase N/A，狀態未知，預計納入 70 人，比較 EUS 導引下線圈合併 cyanoacrylate 注射 vs. BRTO 治療胃靜脈曲張。此試驗雖非直接針對 STS，但反映該疾病領域目前的介入性治療研究方向。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8886633](https://pubmed.ncbi.nlm.nih.gov/8886633/) | 1996 | RCT | Endoscopy | 前瞻性 RCT：高滲葡萄糖水 vs STS 治療胃靜脈曲張出血，比較療效與併發症率 |
| [1734694](https://pubmed.ncbi.nlm.nih.gov/1734694/) | 1992 | RCT | Am J Gastroenterol | STS vs polidocanol 硬化治療食道靜脈曲張，兩組根除率皆達 88%，無顯著差異 |
| [8287811](https://pubmed.ncbi.nlm.nih.gov/8287811/) | 1993 | RCT | Endoscopy | 雙盲 RCT：3% STS vs 5% ethanolamine oleate 治療出血性食道靜脈曲張（95 名患者） |
| [2279644](https://pubmed.ncbi.nlm.nih.gov/2279644/) | 1990 | RCT | Gastrointest Endosc | STS vs sodium morrhuate 治療急性食道靜脈曲張出血，比較死亡率與止血效果 |
| [30170340](https://pubmed.ncbi.nlm.nih.gov/30170340/) | 2019 | Review | J Gastroenterol Hepatol | BRTO（球囊阻斷逆行性經靜脈閉塞術）最新進展回顧，STS 泡沫為 ethanolamine oleate 替代方案 |
| [28180928](https://pubmed.ncbi.nlm.nih.gov/28180928/) | 2017 | Cohort | Cardiovasc Intervent Radiol | 評估 STS + Lipiodol 泡沫用於 BRTO 治療大型門體分流與胃底靜脈曲張之安全性與療效 |
| [3443730](https://pubmed.ncbi.nlm.nih.gov/3443730/) | 1987 | Cohort | J Clin Gastroenterol | 前瞻性研究：STS 硬化治療對食道組織的臨床與病理影響（24 名患者屍檢分析） |
| [37745308](https://pubmed.ncbi.nlm.nih.gov/37745308/) | 2023 | Cohort | Diagn Interv Radiol | 順行性泡沫硬化治療用於門脈高壓性靜脈曲張出血的實用性評估 |
| [21353984](https://pubmed.ncbi.nlm.nih.gov/21353984/) | 2011 | Case series | J Vasc Interv Radiol | BRTO 使用 STS 泡沫取代 ethanolamine oleate 治療出血性胃靜脈曲張之初步經驗 |
| [23064824](https://pubmed.ncbi.nlm.nih.gov/23064824/) | 2012 | Case report | Vasc Endovascular Surg | BRTO 使用 STS 治療胃靜脈曲張時球囊阻斷導管破裂之發生率與處置 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **資料缺口提醒**：本 Evidence Pack 中「TFDA 仿單警語/禁忌」（DG001）標記為 **Blocking** 等級，缺乏此資料將**無法完成 S1 安全性初評**。儘管本項預測已進入 S3 決策階段並建議「Proceed with Guardrails」，此安全性資料缺口仍應優先補齊，否則後續風險評估基礎不足。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 4 篇歷史 RCT（1990–1996）與多篇世代研究直接證實 STS 用於食道／胃靜脈曲張硬化治療的療效，證據等級達 L1，機轉合理性高（同屬血管內硬化作用）。
- 然而本藥品目前**未於香港上市**（0 張許可證），且**原適應症、MOA、仿單安全性資料均為 Data Gap**，其中仿單警語/禁忌屬 Blocking 等級缺口，直接影響安全性初評完整性。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌症資料（DG001，Blocking，需下載仿單 PDF 解析）
- 查詢 DrugBank API 取得完整作用機轉資料（DG002，High）
- 確認香港（或其他鄰近市場）是否已核准 STS 用於食道靜脈曲張相關適應症，作為法規路徑參考
- 補充「食道靜脈曲張（有出血）」與「無出血」兩項預測適應症的臨床試驗現況比對，釐清是否需分別評估急性期止血與預防性治療兩種臨床情境
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

