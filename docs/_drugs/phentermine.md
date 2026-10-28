---
layout: default
title: Phentermine
parent: 僅模型預測 (L5)
nav_order: 691
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "PHENTERMINE"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
description: "Phentermine：預測新適應症為維生素過多症 (hypervitaminosis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Phentermine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Phentermine: 維生素過多症 (hypervitaminosis)
{: .text-alpha }

## 一句話總結

Phentermine 是一種擬交感神經胺類的食慾抑制劑，原本用於肥胖症（含單基因肥胖）與低血壓相關適應症。
TxGNN 模型預測它可能對 **維生素過多症 (Hypervitaminosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 維生素過多症 (hypervitaminosis) |
| TxGNN 預測分數 | 0.9957 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效 11 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Phentermine 主要透過促進去甲腎上腺素釋放（程度較低者還有多巴胺與血清素）來抑制食慾。

維生素過多症源於維生素攝取過量，食慾抑制並沒有已知的途徑可以治療此疾病。因此，這項預測**缺乏合理的機轉連結**，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而非生物學證據。

### 其他預測的補充觀察

| 排名 | 預測疾病 | 分數 | 評估 |
|------|---------|------|------|
| 2 | 16p11.2 近端微缺失症候群 | 0.9949 | 間接且推測性。此症候群常伴嚴重早發肥胖與食慾亢進，與原適應症有重疊，是四個候選中生物學上最合理者；但無法處理神經發展問題，且擬交感神經刺激對癲癇或神經精神共病患者可能有風險 |
| 3 | Hypertelorism（已淘汰術語） | 0.9941 | 無合理機轉；屬顱顏結構異常，且可能是本體論的人為產物 |
| 4 | Frontorhiny | 0.9904 | 無合理機轉；屬先天顱顏畸形，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而非生物學證據 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 11 張有效的單一成分許可證（無已註銷者），許可證資料未登載核准適應症文字與劑型。主要許可證如下：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-33022 | REDUSA CAP 15MG | 膠囊 | 未登載 |
| HK-19830 | DUROMINE CAP 30MG | 膠囊 | 未登載 |
| HK-28878 | DUROMINE CAP 40MG CONTROLLED RELEASE | 控釋膠囊 | 未登載 |
| HK-19829 | DUROMINE CAP 15MG | 膠囊 | 未登載 |
| HK-33023 | REDUSA FORTE CAP 35MG | 膠囊 | 未登載 |

---

## 安全性考量

- **知識圖譜標示的相關疾病（禁忌／需謹慎）**：高血壓、充血性心衰竭、心血管疾病、心臟傳導疾病、心臟瓣膜疾病、肺高壓、心因性猝死、精神病性疾患（含思覺失調、情感性思覺失調）、物質濫用／依賴、第 1 型糖尿病與糖尿病酮酸中毒、青光眼、甲狀腺機能亢進（含 Graves 病）、閉塞性動脈硬化、子癇前症。此資料來自知識圖譜，並非仿單文字。
- **藥物交互作用**（共查得 100 筆，以下為部分）：
  - 重大 (Major)：Tramadol、Bupropion、Methylene blue
  - 中度 (Moderate)：Fentanyl、Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol、Formoterol、Amitriptyline、Ethanol、Metformin、Pioglitazone 等

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（0.9957），但沒有任何臨床試驗或文獻，也找不到合理的機轉連結，證據等級僅 L5。
- 本藥有顯著心血管與精神方面的安全顧慮，在缺乏療效訊號的情況下不宜推進。

**若要推進需要：**
- 取得 Phentermine 的作用機轉資料，並重新評估機轉連結
- 取得香港仿單的警語與禁忌資料
- 若有興趣，可優先探索「16p11.2 近端微缺失症候群」的肥胖表型，先蒐集病例或登記資料，再考慮是否值得研究
- 對維生素過多症、Hypervitaminosis、Hypertelorism 與 Frontorhiny 這幾項預測，除非出現新證據，否則不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

