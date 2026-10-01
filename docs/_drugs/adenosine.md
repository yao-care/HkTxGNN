---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Adenosine：從原適應症（資料未載明）到束支傳導阻滯（已淘汰術語）

## 一句話總結

Adenosine（腺苷）在香港已上市，但本次資料中沒有記載原適應症。
TxGNN 模型預測它可能對**束支傳導阻滯 (obsolete bundle branch block)** 有效。
這個預測目前沒有任何臨床試驗或文獻支持，且該疾病名稱在本體論中已被標為「淘汰」。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 束支傳導阻滯 (obsolete bundle branch block) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。因此無法用輸入資料檢驗 adenosine 對束支傳導阻滯是否有機轉上的合理性。

已知 adenosine 會抑制房室結傳導。對已有傳導阻滯的患者，這種作用不但無法治療，還可能使情況惡化。所以從機轉推論，這個預測並不合理。

此外，「obsolete bundle branch block」是本體論中被標示為淘汰的疾病名稱，很可能是舊版或重複的節點，不是臨床上可執行的適應症。高分可能只是模型在知識圖譜上的假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43112 | ADENOSCAN INJ 3MG/ML | SANOFI HONG KONG LIMITED |
| HK-18525 | HEPATOSWISS FOR IV INFUSION INJ | WILCOME PHARMACEUTICAL CO LTD |
| HK-18057 | HEPATOSWISS IM INJ | WILCOME PHARMACEUTICAL CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，依上述機轉推論，adenosine 的房室結抑制作用可能加重既有的傳導阻滯，這是本預測的主要安全疑慮。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有試驗或文獻佐證，疾病名稱本身也已淘汰。
- adenosine 的已知電生理作用不支持用於傳導阻滯，甚至可能有害。

**若要推進需要：**
- 確認該疾病節點對應到目前有效的疾病術語，或確認它只是重複節點
- 補齊 adenosine 的作用機轉資料（DrugBank）
- 取得香港衞生署仿單的警語、禁忌與核准適應症
- 若確認無有效對應，建議不再往此方向投入

**補充觀察（排名第 2 的預測）：**
TxGNN 對**兒茶酚胺敏感型多形性心室頻脈 (CPVT)** 的預測分數為 99.42%，證據等級為 L4，屬於「研究問題」而非治療建議。
- **臨床試驗：** 僅有 1 個 Phase 2a 試驗（NCT07263139，10 人，招募中），但試驗藥物是 AGP100，與 adenosine 無關。
- **文獻：** 有 1 篇個案報告（PMID 18313614）指出 adenosine triphosphate (ATP) 可終止 CPVT 的雙向性心室頻脈，另有 ATP 與 RyR2 的前臨床研究。這些都不是 adenosine 本身的證據。
- **後續方向：** 若要探索，較合理的問題是急性終止心律或診斷用途，不是長期治療。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

