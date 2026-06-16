---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol：從高血壓/心臟衰竭到惡性腎血管性高血壓

## 一句話總結

Carvedilol 是一種同時阻斷 β1、β2 與 α1 腎上腺素受體的多重阻斷劑，廣泛用於高血壓與心臟衰竭的治療。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
惟目前**無臨床試驗**登記、亦**無直接文獻**支持此特定適應症，屬純模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、慢性心臟衰竭（香港無上市許可，依機轉描述推定） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Carvedilol 是一種非選擇性 β 阻斷劑（β1/β2）兼 α1 阻斷劑。它透過 **β1 阻斷**降低心輸出量與腎素分泌，並透過 **α1 阻斷**降低周邊血管阻力，理論上對惡性高血壓的快速降壓有所助益。

惡性腎血管性高血壓（Malignant Renovascular Hypertension）的核心病理在於腎動脈狹窄引發腎臟血流高度依賴 Angiotensin II 維持，此時使用非選擇性 β 阻斷劑存在潛在顧慮：β 阻斷會抑制腎素分泌並可能惡化腎功能，β2 阻斷則可能加重支氣管收縮，在已有器官損傷的惡性病程中增添用藥複雜度。

TxGNN 模型可能透過知識圖譜中高血壓相關節點的共病網絡連結偵測到此關聯，機轉假說雖具一定合理性，但臨床轉譯尚缺直接證據支撐，需審慎評估安全性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Carvedilol 目前在香港**未上市**，無任何藥物許可證登記。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：依據 Evidence Pack 中的機轉描述，以下潛在安全疑慮值得關注：
> - **腎血管性高血壓中的腎功能風險**：腎動脈狹窄患者的腎血流依賴 Ang II，β 阻斷劑可能惡化腎臟灌流。
> - **支氣管收縮風險**：β2 阻斷效應在有呼吸道共病的患者中需謹慎。
> - **低血糖症狀掩蓋**：β 阻斷劑可能掩蓋糖尿病患者的低血糖警示症狀。

---

## 結論與下一步

**決策：Hold**

**理由：**
Evidence Pack 中所有 5 個預測適應症均為 L5 等級（純模型預測），針對惡性腎血管性高血壓無任何臨床試驗登記或直接文獻支持；加之 Carvedilol 在腎動脈狹窄情境下的腎功能安全疑慮尚未釐清，此時推進再利用風險過高。

**若要推進需要：**
- 取得 Carvedilol 完整作用機轉資料（DrugBank API 查詢，補足 DG002）
- 取得香港/台灣原廠仿單，確認完整警語與禁忌症（補足 DG001）
- 搜尋文獻：Carvedilol 於惡性高血壓或腎血管性高血壓的個案報告或回顧性研究
- 若上述文獻蒐集後仍為空白，建議將研究資源轉向 Rank 3（肺高壓相關適應症），該適應症具有較豐富的一般機轉文獻基礎，且 Group 1 PAH（動脈性肺高壓）中已存在少數 carvedilol 探索性研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

