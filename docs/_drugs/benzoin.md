---
layout: default
title: Benzoin
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Benzoin
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

# Benzoin：從傳統防腐外用藥到外陰陰道念珠菌感染

## 一句話總結

Benzoin（安息香）是一種傳統植物性樹脂，以外用防腐與皮膚保護用途為主，香港目前無核准藥品許可證。TxGNN 模型預測其最高分適應症為**外陰陰道念珠菌感染 (Vulvovaginal Candidiasis)**，預測分數達 97.79%，然而此適應症目前**無任何臨床試驗或文獻**直接支持，整體證據基礎薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症（傳統外用：防腐、皮膚保護、薰吸） |
| 預測新適應症 | 外陰陰道念珠菌感染 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 97.79% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Benzoin（安息香）是來自安息香屬（*Styrax* spp.）植物的天然樹脂，主要活性成分包含**苯甲酸（benzoic acid）**、桂皮酸苄酯（benzyl cinnamate）及香草醛（vanillin）。歷史上以 Compound Tincture of Benzoin（安息香複方酊劑）形式廣泛應用於外傷護理、皮膚保護及呼吸道薰吸，屬傳統外用製劑。

就念珠菌感染而言，苯甲酸在體外實驗中對多種真菌（包括 *Candida* spp.）具有一定的抑制活性，理論機轉可能涉及破壞真菌細胞膜完整性或干擾胞內酸鹼代謝。這可能是 TxGNN 模型將 Benzoin 預測用於外陰陰道念珠菌感染的主要依據。

然而，苯甲酸直接應用於陰道黏膜在臨床上存在明顯疑慮：苯甲酸為酸性物質，與正常陰道 pH 的相容性未知，且具潛在黏膜刺激性。此適應症目前完全缺乏臨床前動物研究或人體試驗的直接支持，預測結果僅停留在模型推斷層面，尚無科學依據確認其臨床可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Benzoin 在香港目前無核准藥品許可證登記，屬於未上市藥物。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（97.79%），但外陰陰道念珠菌感染適應症完全缺乏支持的臨床試驗與文獻，證據等級僅為 L5（純模型預測）。Benzoin 在香港未上市，陰道局部給藥的安全性與劑型可行性均未經驗證，目前不具備推進條件。

> **⚠️ 值得注意**：在 TxGNN 前 10 個預測適應症中，排名第 3 的**人類乳頭瘤病毒感染 (HPV Infection)**（預測分數 96.59%）具有 **13 篇文獻**支持，其中包含 2 篇比較研究（RCT / Comparative Study）。歷史上 Benzoin 確曾以複方酊劑賦形劑（tincture of benzoin compound）形式廣泛用於尖銳濕疣（condyloma acuminata）的 Podophyllin 治療，此適應症證據等級達 **L4**，若進行進一步評估，相對更具研究潛力。

**若要推進需要：**
- 體外（in vitro）及動物（in vivo）抗念珠菌活性研究，確認苯甲酸對 *Candida* 的有效濃度與安全窗口
- 陰道局部給藥劑型的安全性評估（pH 相容性、黏膜刺激性測試）
- 補充完整作用機轉（MOA）資料（建議查詢 DrugBank API）
- 補充安全性資訊（仿單警語、禁忌症）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

