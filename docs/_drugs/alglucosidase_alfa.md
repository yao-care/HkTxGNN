---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Alglucosidase Alfa：預測新適應症為成人多葡聚醣體病 (Adult Polyglucosan Body Disease)（證據等級 L5）。原適應症：肝醣儲積症（glycogen storage disease）"
monitor_inn: "ALGLUCOSIDASE ALFA"
predicted_indications: ["adult polyglucosan body disease", "congenital entropion", "congenital ectropion", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "epiblepharon", "ptosis-strabismus-ectopic pupils syndrome"]
---

# Alglucosidase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Alglucosidase Alfa：從肝醣儲積症到成人多葡聚醣體病
{: .text-alpha }

## 一句話總結

Alglucosidase alfa 是重組酸性 α-葡萄糖苷酶（acid alpha-glucosidase），原本用於肝醣儲積症（glycogen storage disease，主要為龐貝氏症）的酵素替代治療。
TxGNN 模型預測它可能對**成人多葡聚醣體病 (Adult Polyglucosan Body Disease, APBD)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測，機轉上的合理性也偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肝醣儲積症（glycogen storage disease） |
| 預測新適應症 | 成人多葡聚醣體病 (Adult Polyglucosan Body Disease) |
| TxGNN 預測分數 | 0.9947 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，alglucosidase alfa 是補充溶小體（lysosome）內酸性 α-葡萄糖苷酶的酵素替代藥物，用於分解溶小體內的肝醣。

APBD 由肝醣分支酶（GBE1）缺乏引起，導致分支不良的多葡聚醣在神經元與星狀膠細胞累積。兩者同屬肝醣代謝異常，這是模型預測的可能依據，但連結是間接的。

機轉上的限制相當明顯：多葡聚醣主要堆積在細胞質，而此酵素預期無法穿越血腦屏障，也不易進入細胞質，因此療效的機轉依據薄弱。0.995 的高分僅為運算預測，不代表實際療效。

### 其他預測適應症（皆為 L5，無試驗或文獻）

| 排名 | 預測疾病 | 分數 | 評估 |
|------|---------|------|------|
| 4–10 | 先天性眼瞼內翻、眼瞼外翻、先天性 Horner 症候群、上睑下垂-聲帶麻痺症候群等眼部／先天性畸形 | 0.9910–0.9922 | 無合理機轉，推測為模型假象，Hold |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56437 | MYOZYME FOR INJ 50MG（廠商：SANOFI HONG KONG LIMITED） | 未提供 | 未提供 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗與文獻佐證（L5）。
- 排名第一的 APBD 在機轉上有疑慮（酵素難以進入腦與細胞質），其餘多為不同酵素缺陷或與肝醣代謝無關的先天性畸形，模型分數高的原因是分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA），並評估酵素能否到達神經組織與細胞質。
- 進行前臨床研究（APBD 細胞或動物模型），驗證是否能減少多葡聚醣累積。
- 取得香港原廠仿單，補齊核准適應症、警語與禁忌症。
- 系統性檢索 APBD 與 GSD IV 的文獻與試驗登記，確認是否有未被收錄的證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

