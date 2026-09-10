---
layout: default
title: Oxaliplatin
parent: 高證據等級 (L1-L2)
nav_order: 547
evidence_level: L2
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

# Oxaliplatin：從鉑類化療藥物到惡性肋膜間皮瘤

## 一句話總結

Oxaliplatin 是第三代鉑類化療藥物，目前尚未在香港取得藥品許可證。
TxGNN 模型預測它可能對**惡性肋膜間皮瘤 (Malignant Pleural Mesothelioma)** 有效，
目前有 **5 個臨床試驗**和 **20 篇文獻**支持這個方向，其中 2 個已完成的 Phase 2 試驗直接以 oxaliplatin 治療此適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前無香港許可證資料（本藥未在香港上市，原適應症資訊缺失） |
| 預測新適應症 | 惡性肋膜間皮瘤 (Malignant Pleural Mesothelioma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Oxaliplatin 屬於第三代鉑類烷化劑，透過形成 DNA 鏈間交聯（DNA cross-linking）抑制腫瘤細胞的 DNA 複製與轉錄，進而誘導細胞凋亡。這個機轉與同為鉑類的 cisplatin、carboplatin 相同家族。

惡性肋膜間皮瘤的標準治療（pemetrexed + platinum）本身就是以鉑類藥物為骨幹，顯示鉑類化合物在此適應症中已有明確的臨床角色。Oxaliplatin 雖非目前的第一線鉑類選擇，但機轉上與 cisplatin/carboplatin 高度相似，外推合理性高，這也是 TxGNN 模型給出資料集中最高分之一（0.997）的原因。

文獻證據顯示，oxaliplatin 與 raltitrexed、gemcitabine、vinorelbine 等藥物合併使用，已在多個小型 Phase 2 試驗中被驗證於惡性肋膜間皮瘤患者身上，進一步支持這個預測方向並非單純的模型外推，而是有實際臨床探索基礎。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | 完成 | 29 | Oxaliplatin + Gemcitabine 作為 MPM 一線/二線化療的療效評估 |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | 未知 | 29 | Velcade (bortezomib) + Eloxatin (oxaliplatin) 用於已治療過的 MPM 患者 |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | 未知 | 1000 | PIPAC/PITAC 腹腔內加壓氣霧化療多中心登錄研究，涵蓋惡性肋膜與腹膜疾病 |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | 招募中 | 345 | NX-1607（CBL-B 抑制劑）於晚期惡性腫瘤的首次人體試驗，oxaliplatin 非研究藥物 |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | 尚未招募 | 30 | Cadonilimab 合併化療用於局部晚期食道胃接合部/胃癌之新輔助治療 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase2 trial | Tumori | Oxaliplatin + raltitrexed 治療不可手術 MPM 的先導研究 |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase2 trial | Clinical Lung Cancer | Gemcitabine + oxaliplatin 多中心 Phase 2 試驗，25 位患者入組 |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase2 trial | J Clin Oncol | Raltitrexed + oxaliplatin 合併療法 Phase 2 試驗，70 位患者入組 |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase2/retrospective | J Occup Med Toxicol | Gemcitabine + oxaliplatin 於 pemetrexed 治療後患者的觀察性研究 |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase2 trial | Lung Cancer | Vinorelbine + oxaliplatin 作為 MPM 一線治療的 Phase 2 試驗 |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase2 trial | Lung Cancer | Raltitrexed-oxaliplatin 二線治療 MPM 未見客觀反應（陰性結果） |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Cohort/Review | Eur J Cancer | Institut Gustave Roussy 163 位間皮瘤患者化療/化學免疫療法經驗回顧 |
| [26526504](https://pubmed.ncbi.nlm.nih.gov/26526504/) | 2015 | Review | Cancer Treat Rev | Vinca alkaloids 於 MPM 治療角色回顧，含鉑類合併療法背景 |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sci | Cisplatin、oxaliplatin、pemetrexed 對免疫檢查點表現的影響 |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | Antifolates（含 raltitrexed/oxaliplatin 合併方案）於 MPM 的角色 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（第三代鉑類烷化劑） |
| 骨髓抑制風險 | 中度（鉑類藥物常見嗜中性白血球減少、血小板減少） |
| 致吐性分級 | 中至高度（鉑類藥物屬中高致吐風險，需預防性止吐處置） |
| 監測項目 | CBC（含白血球分類）、肝腎功能、電解質、周邊神經功能評估 |
| 處置防護 | 需依細胞毒性藥物處置規範操作（配製、輸注、廢棄物處理） |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 2 個完成的 Phase 2 試驗直接以 oxaliplatin 合併方案治療惡性肋膜間皮瘤，加上鉑類藥物本身就是此適應症標準治療骨幹，機轉外推合理性高；但試驗規模皆小（<30 人）且部分結果為陰性或狀態未知，證據強度僅達 L2，尚不足以直接支持藥證申請。

**若要推進需要：**
- 補齊 TFDA/香港藥監機構的仿單警語與禁忌症資料（DG001，屬 Blocking 等級缺口）
- 補齊完整作用機轉資料（DG002）
- 確認香港上市/許可證申請路徑（目前未上市）
- 具體的骨髓抑制與周邊神經毒性監測方案
- 更大規模、對照設計的 Phase 2/3 試驗數據佐證
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

