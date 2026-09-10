---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lopinavir：從 HIV 感染治療到貓科後天免疫缺陷症候群

## 一句話總結

Lopinavir 是蛋白酶抑制劑類抗病毒藥物，原用於人類 HIV 感染治療（常與 ritonavir 併用組成 HAART 療法）。
TxGNN 模型評分最高的預測適應症為**貓科後天免疫缺陷症候群 (Feline AIDS / FIV 相關疾病)**，
但這是非人類（獸醫）疾病實體，目前**無任何臨床試驗或文獻**支持，證據等級僅 **L5**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無許可證資料（香港未上市，Evidence Pack 未收錄核准適應症） |
| 預測新適應症 | 貓科後天免疫缺陷症候群 (Feline AIDS) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（original_moa 列為資料缺口）。但從本 Evidence Pack 收錄的文獻摘要可確認，
lopinavir/ritonavir (LPV/RTV) 屬於 HIV-1 蛋白酶抑制劑，臨床上作為人類 HAART 處方的一部分，
機轉為抑制病毒 Gag-Pol 多蛋白前驅物裂解，阻斷病毒顆粒成熟。

貓科後天免疫缺陷症候群由貓免疫缺陷病毒 (FIV) 引起，FIV 與 HIV 同屬 lentivirus（慢病毒）家族，
兩者蛋白酶結構具部分保守性，這是 TxGNN 給出高分關聯的可能生物學基礎。

然而，Evidence Pack 本身對此候選的機轉說明已明確指出：「雖同屬 lentivirus 蛋白酶抑制概念上可類推，
但無任何人類或動物臨床/文獻資料支持，純屬 TxGNN 知識圖譜上的拓樸相似性推論」。且 FIV 相關疾病屬獸醫適應症，
非人類疾病，即使機轉假說成立，也無法直接轉譯為人用藥品的新適應症申請。因此本候選屬於「概念上可類推、但證據極弱」的類型。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
三個 TxGNN 預測候選證據等級均僅 L4-L5。最高分候選（貓科 FIV 相關疾病）為獸醫適應症，
無任何人類或動物臨床/文獻證據；次高分候選（simian immunodeficiency virus infection）雖有 3 篇文獻，
但均為 macaque 動物模型下合併抗反轉錄病毒療法（含 lopinavir/ritonavir）的觀察性研究，非單一藥物人體適應症證據；
第三候選（罕見神經發育疾病）與 lopinavir 機轉無已知生物學關聯，判斷為模型端假陽性。整體證據不足以支持推進人體臨床開發。

**若要推進需要：**
- 補齊 lopinavir 完整 MOA 與 TFDA/香港仿單安全性資料（目前為 Blocking 等級資料缺口）
- 重新檢視 TxGNN 候選清單，排除獸醫適應症，聚焦與 lopinavir 已知蛋白酶抑制機轉直接相關的人類病毒感染疾病
- 若持續看好慢病毒（lentivirus）感染方向，需補充人類臨床或至少人類病毒株體外藥效資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

