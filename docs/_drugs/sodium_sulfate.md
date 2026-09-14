---
layout: default
title: Sodium Sulfate
parent: 僅模型預測 (L5)
nav_order: 695
evidence_level: L5
indication_count: 1
---

# Sodium Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sodium Sulfate：從腸道製劑成分到消化不良（Dyspepsia）

## 一句話總結

Sodium Sulfate（DB09472）常見於腸道製劑（如大腸鏡前腸道準備）中的滲透性瀉劑成分，目前在香港未上市，亦無登記的原適應症資料。TxGNN 模型預測其對**消化不良 (Dyspepsia)** 可能有效，但現有的 3 個臨床試驗與 4 篇文獻**均未直接支持**這個關聯，證據等級僅為 L5（純模型預測），且部分文獻疑似因藥名混淆（與 Dextran Sodium Sulfate 誤配）而產生偽陽性關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無登記資料（香港未上市，無許可證/適應症紀錄） |
| 預測新適應症 | 消化不良 (Dyspepsia) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L5（僅模型預測，無實際支持研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏 Sodium Sulfate 的詳細作用機轉（MOA）資料。根據 Evidence Pack 中的機轉關聯分析，Sodium Sulfate 屬於滲透性瀉劑/腸道製劑成分（例如用於大腸鏡檢查前的腸道準備），其藥理作用是透過滲透壓效應促使腸道排空，與消化不良（上消化道不適/功能性消化不良）的病理機轉**沒有已知的生物學關聯**。

更需注意的是，文獻檢索中出現多篇提及 "Dextran Sodium Sulfate (DSS)" 的動物實驗（用於誘導結腸炎模型），這是一種**完全不同的化學試劑**，僅因名稱含有 "Sodium Sulfate" 字樣而被誤配對，並非真正支持 Sodium Sulfate 本身對 dyspepsia 的療效證據。因此，這個預測在機轉層面**缺乏合理性**，目前應視為模型層級的低置信度假說，而非有實證支持的候選方向。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06339697](https://clinicaltrials.gov/study/NCT06339697) | Phase 4 | 完成 | 194 | 評估不同腸道準備瀉劑（含硫酸鈉類滲透劑）對腸道菌相之短期影響；終點為菌相變化，非 dyspepsia 療效（相關性：中） |
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | 招募中 | 140 | 比較 Alginate 與 Sucralfate 治療 GERD 症狀，未使用 Sodium Sulfate（相關性：低） |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | 未知 | 150 | 比較 Oxycodone 與 Pregabalin 之術後鎮痛效果，與本藥物或 dyspepsia 無直接關聯（相關性：低） |

**註**：以上 3 個試驗均**未直接測試 Sodium Sulfate 對 dyspepsia 的療效**，僅因疾病領域或藥物類別部分重疊被系統匹配。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | 動物實驗 | Molecules | 探討 Dextran Sodium Sulfate（DSS，非本藥物）誘導腸道損傷對 Donepezil 藥動學之影響 |
| [34207410](https://pubmed.ncbi.nlm.nih.gov/34207410/) | 2021 | 動物實驗 | Pharmaceuticals | DSS 誘導腸道損傷加重 Galantamine 對胃電活動之影響 |
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | 動物實驗（結腸炎模型） | Int J Mol Sci | Atractylodin 透過 PPARα 途徑改善結腸炎，與 Sodium Sulfate 無關 |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | 動物實驗（結腸炎模型） | J Inflamm Res | 中藥四逆湯對潰瘍性結腸炎的網絡藥理學研究，與 Sodium Sulfate 無關 |

**註**：以上 4 篇文獻**均為 Tier 3（動物/臨床前研究）**，且其中 2 篇提及的 "Dextran Sodium Sulfate (DSS)" 為疾病模型誘導試劑，與本藥物 Sodium Sulfate 為不同化合物，屬名稱混淆導致的間接匹配，**非直接支持證據**。

---

## 香港上市資訊

目前無香港上市許可證登記（`total_licenses = 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠ 注意：本藥物的安全性資料（主要警語、禁忌症、藥物交互作用）目前皆為資料缺口，且此缺口被標記為 **Blocking（阻斷級）**，無法進行 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5，現有臨床試驗與文獻均未直接支持 Sodium Sulfate 對 dyspepsia 的療效，且部分文獻證據疑似因與 Dextran Sodium Sulfate（DSS）名稱混淆而產生偽陽性配對。
- 缺乏作用機轉（MOA）資料，無法建立生物學合理性；同時安全性資料（仿單警語、禁忌症）為 Blocking 缺口，尚無法進行安全性初評。

**若要推進需要：**
- 補齊 Sodium Sulfate 的作用機轉（MOA）資料（來源：DrugBank API）
- 取得官方仿單警語與禁忌症資料，解除安全性評估的阻斷缺口
- 重新檢視文獻檢索策略，排除因 "Dextran Sodium Sulfate" 名稱混淆造成的偽陽性配對
- 若後續要繼續此候選方向，需尋找真正以 Sodium Sulfate（非 DSS）為介入藥物、且以 dyspepsia 為終點的人體研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

