---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 446
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir：從 CMV 感染預防到外陰陰道念珠菌感染

## 一句話總結

Letermovir 是 CMV terminase 複合體抑制劑，原本用於造血幹細胞移植後的巨細胞病毒 (CMV) 感染預防。
TxGNN 模型預測它可能對**外陰陰道念珠菌感染 (Vulvovaginal Candidiasis)** 有效，
但目前**沒有任何臨床試驗或文獻證據**支持這個方向，機轉上也找不到合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | CMV 感染預防（造血幹細胞移植後）；本地無許可證資料 |
| 預測新適應症 | 外陰陰道念珠菌感染 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.88%（排名 3074） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Letermovir 是專一性 CMV terminase 複合體抑制劑（作用於 pUL56/pUL89/pUL51），
透過阻斷病毒 DNA 包裝來抑制 CMV 複製，臨床上用於造血幹細胞移植後的 CMV 感染預防。

外陰陰道念珠菌感染則是由 *Candida albicans* 過度增生及黏膜免疫失衡所致的真菌感染，
致病機轉與病毒複製抑制完全不同路徑。

目前**找不到生物合理性支持**這項預測：Letermovir 沒有已知的抗真菌活性，也沒有文獻顯示其具備免疫調節或黏膜屏障相關作用。TxGNN 給出的高分（99.88%）很可能是知識圖譜中節點鄰近性造成的偽陽性，而非真實的藥理關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本地藥物安全性資料（警語、禁忌症、DDI）目前缺失（Data Gap DG001，屬 Blocking 等級），且作用機轉資料亦不完整（DG002），這兩項缺口本身就足以擋下任何後續評估。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上無合理連結，TxGNN 高分疑似為知識圖譜偽陽性，缺乏生物合理性基礎
- 零臨床試驗、零文獻支持，證據等級僅 L5
- 本地未上市（0 張許可證），且安全性資料為 Blocking 等級的資料缺口，尚無法進入 S1 安全性初評

**若要推進需要：**
- 補齊 TFDA/當地仿單的警語與禁忌症資料（DG001，Blocking）
- 補齊 Letermovir 完整作用機轉資料（DG002）
- 尋找是否有抗真菌活性或黏膜免疫相關的機轉研究，重新評估生物合理性
- 若持續缺乏機轉與證據支持，建議停止此候選的後續投入
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

