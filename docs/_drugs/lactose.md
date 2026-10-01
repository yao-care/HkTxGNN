---
layout: default
title: Lactose
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Lactose
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

# Lactose：從製劑賦形劑到食道靜脈曲張（未出血）

## 一句話總結

Lactose（乳糖）在香港的登記產品中作為藥品成分出現，沒有登記獨立的原適應症。
TxGNN 模型預測它可能對**食道靜脈曲張（無出血，esophageal varices without bleeding）**有效，但唯一關聯的臨床試驗是 tenofovir 的研究，乳糖並非試驗藥物，因此**沒有任何直接支持證據**，這很可能是知識圖譜的假象。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 食道靜脈曲張（無出血，esophageal varices without bleeding） |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。乳糖是一種雙糖，在這 5 張香港許可證的產品中是製劑成分，通常扮演賦形劑的角色，本身沒有已證實的治療用途。

乳糖對門脈高壓或靜脈曲張的病理生理沒有已知作用，也沒有止血、降低門脈壓或血管方面的活性。因此，原成分與新適應症之間找不到合理的機轉關聯。

TxGNN 分數雖高（99.93%，模型排名 1914），但分數本身不等於生物學合理性。這個預測最可能來自知識圖譜的結構性假象，不應視為有效性訊號。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02224456](https://clinicaltrials.gov/study/NCT02224456) | Phase 4 | 完成 | 197 | 評估 tenofovir disoproxil fumarate 用於中國慢性 B 型肝炎合併進行性纖維化或代償性肝硬化患者。乳糖最多是錠劑賦形劑，不是試驗介入，與乳糖療效無關（相關性評級 C） |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43329 | MICROGYNON 30 ED TAB | BAYER HEALTHCARE LIMITED |
| HK-56563 | YAZ TAB | BAYER HEALTHCARE LIMITED |
| HK-68562 | ALYSSA TABLETS | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-65968 | MEDIAZ TABLETS | DKSH HONG KONG LIMITED |
| HK-59784 | QLAIRA TAB | BAYER HEALTHCARE LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測，沒有任何以乳糖為介入的試驗或文獻，唯一關聯的試驗是 tenofovir 研究，與乳糖無關。
- 乳糖是惰性賦形劑，對靜脈曲張沒有合理的機轉。同一份資料中其他 9 個預測適應症也都是 L4–L5、建議 Hold，沒有一個有直接證據。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料。
- 取得香港衛生署仿單的警語與禁忌症。
- 除非能找到以乳糖為活性成分的直接研究，否則建議不投入進一步資源。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

