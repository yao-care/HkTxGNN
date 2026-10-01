---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin：從泌尿科 α1 阻斷劑到 Ambras 型全身性先天性多毛症

## 一句話總結

Alfuzosin 是選擇性 α1 腎上腺素受體拮抗劑，在香港以緩釋錠劑型上市。
TxGNN 模型預測它可能對 **Ambras 型全身性先天性多毛症 (Ambras type hypertrichosis universalis congenita)** 有效。
目前**沒有臨床試驗**和**沒有文獻**支持，這只是圖譜模型的預測，尚無實證。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症 |
| 預測新適應症 | Ambras 型全身性先天性多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Alfuzosin 是選擇性 α1 腎上腺素受體拮抗劑，屬泌尿科症狀治療用藥。

Ambras 症候群是罕見的遺傳性毛髮發育異常疾病，與腎上腺素訊號傳遞沒有已知關聯。因此目前找不到合理的機轉連結。

TxGNN 的高分（約 0.99999）只來自知識圖譜上的關聯，可能反映疾病鄰近區域的圖譜假象，不能視為療效訊號。排名第 2 的「多毛症」也一樣：多毛症是米諾地爾等血管擴張劑的已知副作用，Alfuzosin 對它較可能是中性，而不是治療。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 7 張許可證，以下列出 5 張主要許可證（許可證資料未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67012 | ALFUZOSIN RIVOPHARM PROLONGED-RELEASE TABLETS 10MG | I & C (HONG KONG) LIMITED |
| HK-59835 | APO-ALFUZOSIN PROLONGED-RELEASE TAB 10MG | HIND WING CO LTD |
| HK-47335 | XATRAL XL TAB 10MG | SANOFI HONG KONG LIMITED |
| HK-59623 | ALFURAL PROLONGED RELEASE TAB 10MG | ZENFIELDS (H.K.) LIMITED |
| HK-41468 | XATRAL SR TAB 5MG | SANOFI HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻，也找不到合理的作用機轉，證據等級只有 L5。
- 排名前 10 的預測適應症都沒有可信的藥理連結。排名第 3 的牙周相關疾病雖檢索到 20 篇文獻，但都是一般牙周炎文獻，沒有提到 Alfuzosin，不能算作藥物證據。

**若要推進需要：**
- 取得香港衞生署仿單，確認核准適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉資料，重新評估機轉連結。
- 若要繼續，需先有機轉或前臨床證據支持，再考慮進一步評估。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

