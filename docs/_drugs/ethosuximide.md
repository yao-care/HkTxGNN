---
layout: default
title: Ethosuximide
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 1
---

# Ethosuximide
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

# Ethosuximide：從失神性癲癇到腎源性不適當抗利尿症候群

## 一句話總結

Ethosuximide 是一種 T 型電壓門控鈣離子通道抑制劑，傳統上用於**失神性癲癇**的治療。TxGNN 模型預測它可能對**腎源性不適當抗利尿症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD）** 有效，但目前**無任何臨床試驗或文獻**支持這個預測方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 失神性癲癇（Absence Epilepsy） |
| 預測新適應症 | 腎源性不適當抗利尿症候群（NSIAD） |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉資料。根據現有資訊，Ethosuximide 主要透過抑制視丘神經元上的 **T 型電壓門控鈣離子通道（Cav3.1/Cav3.2）**，阻斷視丘皮質迴路的異常節律放電，從而控制失神性癲癇的發作。這是一個以神經系統為核心的藥理機轉。

NSIAD 是一種罕見的 X 染色體遺傳疾病，病因在於 **AVPR2 基因功能增益突變**，導致腎臟 V2 受體在缺乏抗利尿激素（ADH）的情況下持續活化，進而透過 cAMP/PKA 訊號持續將水通道蛋白 Aquaporin-2（AQP2）插入集尿管頂端膜，造成不依賴 ADH 的自由水滯留與稀釋性低鈉血症。

就機轉關聯性而言，**T 型鈣離子通道抑制與 V2R–cAMP–AQP2 軸之間，目前文獻中沒有任何已知的直接或間接生物機轉連結**。TxGNN 的高預測分數（0.9991）很可能源於知識圖譜拓撲結構中，神經系統節點與罕見病節點之間的圖結構相似性，而非反映真實的生物機轉路徑。本預測屬**高度推測性**，應謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Ethosuximide 的核心藥理機轉（抑制 T 型鈣離子通道）與 NSIAD 的致病路徑（AVPR2 功能增益突變 → V2R 持續活化 → AQP2 水通道滯留）之間缺乏已知的生物學橋梁，且目前完全無臨床試驗或文獻佐證，證據等級僅為 L5（純模型預測），不具備進入下一階段評估的條件。

**若要推進需要：**
- **基礎科學驗證**：在細胞層次測試 Ethosuximide 是否能干擾 cAMP/PKA 訊號或 AQP2 的膜插入機制
- **動物模型實驗**：使用 AVPR2 功能增益突變小鼠模型，觀察 Ethosuximide 對水分代謝與低鈉血症的影響
- **擴展文獻搜尋**：擴大至相關機轉領域（鈣離子訊號與 AQP2 調控、T 型通道與腎臟生理、稀釋性低鈉血症藥物研究）
- **安全性資料補充**：下載並解析仿單 PDF，完成正式安全性初評（S1 階段）
- **孤兒藥可行性評估**：確認 NSIAD 罕見病身分對應的法規路徑與市場規模
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

