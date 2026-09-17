---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 596
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin：從瀰漫性大 B 細胞淋巴瘤到 HER2 陽性乳癌

## 一句話總結

Polatuzumab vedotin 是標靶 CD79b 的抗體-藥物複合體（ADC），核准用於瀰漫性大 B 細胞淋巴瘤（DLBCL）。
TxGNN 模型預測它可能對 **HER2 陽性乳癌 (HER2 positive breast carcinoma)** 有效，
但目前**沒有任何臨床試驗或文獻支持**這個方向，機轉上的關聯性也相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 瀰漫性大 B 細胞淋巴瘤（DLBCL）|
| 預測新適應症 | HER2 陽性乳癌 (HER2 positive breast carcinoma) |
| TxGNN 預測分數 | 99.34%（排名第 11,082 位）|
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Polatuzumab vedotin 標靶 CD79b（B 淋巴球表面抗原），彈頭為 MMAE（微管抑制劑），透過抗體專一性將細胞毒殺分子遞送至表現 CD79b 的 B 細胞系腫瘤細胞。

問題在於：HER2 陽性乳癌細胞並不表現 CD79b，兩者在受體層級缺乏機轉基礎。唯一可能的連結，只是 MMAE 彈頭對快速分裂細胞的非專一性毒殺作用——這是通用化療機轉，而非真正的藥物再利用邏輯。

TxGNN 分數雖高（0.993），但缺乏任何試驗或文獻佐證，判斷較可能是知識圖譜中的拓樸相似性推論（例如經由其他 ADC 或 HER2 標靶藥物節點間接連結），而非具體的生物學關聯。此外，DrugBank 正式查詢未能取得完整 MOA 記錄（列為 High 等級資料缺口），進一步限制了機轉判斷的確定性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 細胞毒性

Polatuzumab vedotin 屬於抗體-藥物複合體（ADC），MMAE payload 具細胞毒性，原適應症（DLBCL）為血液腫瘤。此 Evidence Pack 未取得 DrugBank 的骨髓抑制、致吐性等具體毒性資料，相關監測與處置細節請參考原廠仿單的警語與注意事項。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（ADC，MMAE 微管抑制劑彈頭）|
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
CD79b 與 HER2 缺乏受體層級的機轉關聯，且此適應症配對沒有任何臨床試驗或文獻佐證（evidence level L5，decision stage S0）。加上藥物在香港未上市、TFDA 仿單警語/禁忌資料缺失（Blocking gap DG001）、作用機轉資料未完整取得（DG002），現階段不具備推進基礎。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症資料（DG001，Blocking）
- 透過 DrugBank API 或原廠資料完整確認作用機轉（DG002）
- 尋找 CD79b 或 MMAE payload 與 HER2 陽性乳癌之間的獨立機轉或前臨床研究佐證
- 若後續仍無法找到獨立生物學證據，建議直接關閉此候選而非持續投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

