---
layout: default
title: Latanoprostene Bunod
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 5
---

# Latanoprostene Bunod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Latanoprostene Bunod：從隅角開放性青光眼到 Visceral Calciphylaxis

## 一句話總結

Latanoprostene Bunod（DB11660）為前列腺素類似物合併一氧化氮（NO）供體的眼用降眼壓藥物，原研藥 Vyzulta 核准用於開放性隅角青光眼與高眼壓症。TxGNN 模型將其與 **Visceral Calciphylaxis（內臟型鈣化防禦症）** 配對，預測分數高達 **99.76%**，但目前**無任何臨床試驗或文獻**支持這個方向，也**無可辨識的機轉關聯**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開放性隅角青光眼／高眼壓症（原研藥 Vyzulta 已知適應症；台灣未上市，無許可證資料可查證） |
| 預測新適應症 | Visceral Calciphylaxis |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L5 |
| 台灣上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏本藥物詳細的作用機轉（MOA）資料庫記錄。根據評估資料中已知的外部背景，Latanoprostene Bunod 是 PGF2α 前列腺素類似物並釋放 NO，透過小樑網／葡萄膜鞏膜通路降眼壓，屬局部眼用藥物，全身生體可用率極低。

Calciphylaxis（鈣化防禦症）是小血管鈣化併發血栓性缺血病變，主要致病機轉與副甲狀腺功能亢進、慢性腎臟病（CKD）、鈣磷代謝異常有關，屬全身性血管／代謝疾病。這與一個以局部眼內作用為主、全身暴露量極低的降眼壓藥物之間，**沒有已知的藥理或機轉連結**。

換句話說，這是 TxGNN 知識圖譜在高分區間產出、但缺乏機轉支持、缺乏臨床試驗、缺乏文獻佐證的「純模型預測」配對，屬於探索性假說而非有實證基礎的方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 該預測配對無機轉合理性、無臨床試驗、無文獻支持，屬 L5（純模型分數）等級，尚未達到可進行安全性初評（S1）的門檻。
- 台灣未上市（0 張許可證），亦缺乏 MOA 與仿單警語等基礎資料（Blocking data gap），無法評估在地適用性。

**若要推進需要：**
- 補齊 DrugBank／原廠 MOA 全文，釐清是否有全身性血管或鈣磷代謝相關的次要藥理作用
- 取得 TFDA／原廠仿單警語與禁忌症，完成 S1 安全性初評
- 若欲探索本藥物的老藥新用潛力，建議優先評估同一評估批次中 **rank 2「primary hereditary glaucoma」**——該配對與原適應症（青光眼）機轉直接相關，證據等級為 L4，已進入 S1 階段，科學合理性明顯高於 visceral calciphylaxis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

