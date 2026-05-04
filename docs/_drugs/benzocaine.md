---
layout: default
title: Benzocaine
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 1
---

# Benzocaine
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

# Benzocaine：從局部麻醉到乳突性結膜炎

## 一句話總結

Benzocaine 是一種酯類局部麻醉劑，透過阻斷感覺神經末梢的電壓依賴性鈉離子通道（Nav）來緩解疼痛與搔癢。
TxGNN 模型預測它可能對**乳突性結膜炎 (Papillary Conjunctivitis)** 有效，
然而目前**無任何臨床試驗或文獻**支持此方向，機轉上亦存在多項關鍵疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部麻醉（皮膚及黏膜疼痛、搔癢緩解） |
| 預測新適應症 | 乳突性結膜炎 (Papillary Conjunctivitis) |
| TxGNN 預測分數 | 99.38% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為數據缺口）。根據已知資訊，Benzocaine 是酯類局部麻醉劑，透過穩定神經細胞膜、阻斷電壓依賴性鈉離子通道（Nav channel），抑制動作電位的產生與傳導，達到局部感覺阻斷效果。

乳突性結膜炎的核心症狀包括搔癢、灼熱感及眼部異物感，TxGNN 模型可能基於「局部麻醉 → 感覺神經抑制 → 症狀緩解」的表型相似性做出此預測。然而，此推論存在三項關鍵反向疑慮：

1. **給藥途徑不適合**：眼科局部麻醉的首選藥物為 Proparacaine 或 Tetracaine，Benzocaine 因眼組織穿透性低且對局部 pH 敏感性高，臨床上並不用於眼科。
2. **代謝物過敏風險高**：Benzocaine 水解後產生對胺苯甲酸（PABA），屬高過敏原性代謝物，可能誘發或加劇乳突性結膜炎的免疫反應，與治療目標相悖。
3. **模型過度泛化疑慮**：TxGNN 高分（0.9938）可能源自模型將「局麻 → 發炎症狀改善」的表型相似性過度泛化，缺乏眼科局部應用的特異性機轉依據。

整體而言，機轉關聯性較弱，預測合理性存疑。

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
目前僅有 TxGNN 模型預測支持（L5 證據等級），無任何臨床試驗或文獻佐證，且機轉層面存在給藥途徑不適合、PABA 代謝物過敏風險等重大疑慮，在未取得進一步數據前不建議推進。

**若要推進需要：**
- 補充 Benzocaine 完整作用機轉資料（DrugBank MOA API 查詢）
- 搜尋 Benzocaine 或同類酯類局麻劑用於眼科的前臨床安全性研究
- 評估 PABA 代謝物在眼科局部使用情境下的過敏風險及致敏頻率
- 下載並解析仿單 PDF，確認警語、禁忌與適應症（補足 DG001 數據缺口）
- 比較 Tetracaine 等眼科核准局麻劑的結構差異，評估是否有機轉改良空間
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

