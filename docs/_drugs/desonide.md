---
layout: default
title: Desonide
parent: 中證據等級 (L3-L4)
nav_order: 190
evidence_level: L4
indication_count: 10
---

# Desonide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Desonide：從局部炎症性皮膚病到聲帶息肉

## 一句話總結

Desonide 是一種低效價局部外用糖皮質激素，主要用於輕至中度炎症性皮膚疾病的治療。
TxGNN 模型預測它可能對**聲帶息肉 (Polyp of Vocal Cord)** 有效，
但目前**無臨床試驗**及**無相關文獻**支持這個方向，整體證據基礎極為有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 炎症性皮膚疾病（香港未上市，許可證資料缺失） |
| 預測新適應症 | 聲帶息肉 (Polyp of Vocal Cord) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 資料缺失）。根據已知資訊，Desonide 屬於低效價局部外用糖皮質激素類別，具有抗炎、抗過敏及局部血管收縮作用，對皮膚炎症性疾病（如異位性皮膚炎、接觸性皮膚炎）的療效已有充分文獻支持。

聲帶息肉的部分亞型——尤其是炎症性或水腫性聲帶息肉——在病理上具有顯著的局部炎症成分。從 class-level 角度而言，同類糖皮質激素（如 triamcinolone）局部注射已有案例報告應用於此類炎症性聲帶病變，說明此藥物類別在機轉上存在一定的合理性。

然而，Desonide 屬低效價製劑，且其現有劑型（乳膏、凝膠、乳液）均為外用皮膚製劑。針對聲帶的局部應用（局部注射或吸入途徑）目前完全缺乏研究。此預測屬於 class-level 間接推論，Desonide 本身對聲帶息肉的特異性臨床數據為零。

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
目前僅有 TxGNN 模型預測結果，佐以 class-level 間接機轉推論（L4），無任何 Desonide 用於聲帶息肉的臨床試驗或直接文獻證據。藥物本身在香港未上市，安全性資料亦全數缺失，數據基礎不足以支持進一步推進。

**若要推進需要：**
- 補充 Desonide 詳細作用機轉（MOA）資料（建議查詢 DrugBank API）
- 收集安全性資料：仿單警語、禁忌症（建議下載原廠仿單 PDF 解析）
- 評估給藥路徑可行性：聲帶病變需要局部注射或吸入劑型，現有皮膚外用劑型不適用
- 尋找同類糖皮質激素（corticosteroids）用於炎症性聲帶疾病的臨床試驗或系統性回顧，作為 class-level 間接支持的補充
- 考量是否有更高效價的同類藥物（如 triamcinolone、dexamethasone）已有相關研究，評估 Desonide 的相對開發優先性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

