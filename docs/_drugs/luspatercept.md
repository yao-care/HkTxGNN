---
layout: default
title: Luspatercept
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Luspatercept
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

# Luspatercept：從貧血（β 型地中海型貧血、骨髓增生異常症候群）到 Monosomy X（透納氏症候群）

## 一句話總結

Luspatercept 是一種促進紅血球晚期成熟的注射藥物，用於治療 β 型地中海型貧血與骨髓增生異常症候群（MDS）相關貧血。
TxGNN 模型預測它可能對 **Monosomy X（透納氏症候群）** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測，機轉上也找不到合理的關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | β 型地中海型貧血、MDS 相關貧血（香港許可證未附適應症文字，此處依模型評估資料補充） |
| 預測新適應症 | Monosomy X（透納氏症候群） |
| TxGNN 預測分數 | 96.0% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Luspatercept 是 activin receptor type IIB 的配體捕捉劑（ligand trap）。它透過攔截 TGF-β 超家族配體（如 GDF11、activin），促進紅血球前驅細胞的晚期成熟。因此它對無效紅血球生成（ineffective erythropoiesis）造成的貧血有效。

**坦白說，這個預測目前站不住腳。** Monosomy X（透納氏症候群）是染色體異常疾病，病因是 X 染色體缺失，和紅血球成熟障礙沒有已知的關聯。模型的高分（96.0%）沒有任何機轉、試驗或文獻支持，較可能來自知識圖譜中的間接鄰近關係，不是真正的治療訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67366 | REBLOZYL POWDER FOR SOLUTION FOR INJECTION 25MG | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |
| HK-67367 | REBLOZYL POWDER FOR SOLUTION FOR INJECTION 75MG | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，Luspatercept 的仿單有血栓栓塞風險的標示，若用於有血管或血栓風險的族群需特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗、文獻或合理的作用機轉支持（證據等級 L5），且透納氏症候群的病因與 Luspatercept 的作用路徑無關。
- 其餘 9 個預測適應症同樣沒有任何試驗或文獻，多數也找不到合理的機轉關聯。
- 其中只有「丙酮酸激酶缺乏症（pyruvate kinase deficiency of red cells）」在機轉上有間接的合理性，因為它同樣有無效紅血球生成的成分。目前僅屬研究假設，可列為後續研究問題，不代表已有證據。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料（目前為阻擋性資料缺口）
- 取得 DrugBank 的作用機轉資料
- 針對 Monosomy X 做系統性文獻與試驗檢索，確認是否真有任何研究線索
- 若要優先探索，建議先評估丙酮酸激酶缺乏症這個較合理的候選

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

