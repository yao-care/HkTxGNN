---
layout: default
title: Estradiol Valerate
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Estradiol Valerate
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

# Estradiol Valerate：從原適應症（資料未提供）到 X 染色體脆折症女性帶因者的症狀表現

## 一句話總結

Estradiol Valerate（戊酸雌二醇）是一種雌激素酯類藥物，香港已有 2 張許可證，但本次資料未載明原核准適應症。
TxGNN 模型預測它可能對**女性帶因者的症狀性 X 染色體脆折症 (symptomatic form of fragile X syndrome in female carrier)** 有效，預測分數很高，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性帶因者的症狀性 X 染色體脆折症 (symptomatic form of fragile X syndrome in female carrier) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Estradiol Valerate 是雌激素類藥物，香港的兩張許可證（ESTRADE TAB 2MG、QLAIRA TAB）都是含此成分的口服製劑。但由於原適應症資料也缺漏，無法確認它在原適應症的療效基礎，也無法比對新舊適應症的關聯。

從疾病生物學來看，X 染色體脆折症的前突變 (premutation) 女性帶因者可能發生 FMR1 相關的原發性卵巢功能不全 (primary ovarian insufficiency, POI)。針對這個卵巢表現型，雌激素補充在機轉上有合理性。

但這只是推論。現有資料中沒有任何試驗或文獻支持，模型的高分只是知識圖譜上的關聯，不能視為療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-48266 | ESTRADE TAB 2MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |
| HK-59784 | QLAIRA TAB | BAYER HEALTHCARE LIMITED |

兩張許可證的劑型與核准適應症在資料中均為空白，需另行查證。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何試驗或文獻佐證（L5），機轉推論也缺乏資料支持。
- 香港藥品仿單的警語與禁忌尚未取得，無法進入安全性篩檢。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊核准適應症、警語與禁忌症。
- 補充 DrugBank 的作用機轉資料。
- 針對 FMR1 前突變帶因者的 POI，檢索雌激素補充的臨床與觀察性研究。
- 本次 Evidence Pack 另有 9 個預測適應症。其中「卵巢功能障礙 (ovarian dysfunction)」的機轉最合理（POI 的雌激素補充），但唯一直接相關的 Phase 3 試驗 NCT02922348 已撤銷、零收案。其餘多數為染色體異常類疾病，缺乏可辨識的機轉關聯，建議先從卵巢功能障礙方向釐清。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

