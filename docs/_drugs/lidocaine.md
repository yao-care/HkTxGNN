---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

Using the v5 藥物再利用評估報告 prompt spec to structure this directly from the Evidence Pack (no additional skill applies to this task — it's a documented report-writing format already given in full).

# Lidocaine：從局部麻醉到點狀角結膜上皮炎

## 一句話總結

> Lidocaine 是已知的 amide 類局部麻醉劑（本資料包未收錄其香港核准適應症與作用機轉細節）。
> TxGNN 模型預測它可能對**點狀角結膜上皮炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，
> 但目前**沒有臨床試驗、也沒有文獻**支持這個方向，且僅有的機轉推論反而指向安全疑慮。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未收錄（本資料包無許可證/適應症資料） |
| 預測新適應症 | 點狀角結膜上皮炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Lidocaine 詳細的作用機轉資料（Data Gap，待查 DrugBank）。

更關鍵的是，本候選的機轉推論本身並不支持「治療用途」：局部麻醉藥理論上可暫時緩解角結膜刺激症狀，但已知**長期或反覆的局部麻醉劑暴露反而會誘發或惡化點狀角膜上皮病變**（毒性角膜病變），與治療目的相悖。也就是說，這個預測更像是一個潛在**安全性訊號**，而非可驗證的治療假說。

搭配零筆臨床試驗、零筆文獻的證據狀態，這個排名第一的預測目前不具備進一步評估的基礎。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Lidocaine 目前未於香港上市，資料包中無許可證登記（0 張）。

## 安全性考量

安全性資訊請參考原廠仿單。（本資料包標記「TFDA 仿單警語/禁忌」為 Blocking 等級資料缺口，尚無法完成 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（點狀角結膜上皮炎）零臨床試驗、零文獻，證據等級僅 L5，且唯一的機轉論述指向的是毒性風險而非療效。
- 作用機轉（MOA）與仿單警語兩項關鍵資料皆缺失，其中仿單警語為 Blocking 等級缺口，無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 Lidocaine 完整仿單警語與禁忌症資料（DG001，來源：TFDA 官網仿單 PDF）
- 補齊 DrugBank 作用機轉資料（DG002）
- 若改為評估其他候選（如 rank 5「atopic conjunctivitis」L4 或 rank 6「conjunctival disorder」L2/S1），需先排除文獻誤配問題——rank 6 有近半文獻是因病名字面含 "conjunctival injection and tearing" 而誤收的 SUNCT/SUNA 頭痛症候群研究，且其試驗證據多反映 Lidocaine 既有的眼科手術麻醉用途，而非針對該疾病的新治療訊號
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

