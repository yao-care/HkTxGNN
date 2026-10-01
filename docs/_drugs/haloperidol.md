---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 5
---

# Haloperidol
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

# Haloperidol：從抗精神病用藥到先天性糖基化異常（岩藻糖基化缺陷型）

## 一句話總結

Haloperidol 在香港已有 18 張上市許可證，一般認知是抗精神病藥，但本次資料未載明其核准適應症。
TxGNN 模型預測它可能對**岩藻糖基化缺陷型先天性糖基化異常 (Congenital disorder of glycosylation with defective fucosylation)** 有效，
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 岩藻糖基化缺陷型先天性糖基化異常 (Congenital disorder of glycosylation with defective fucosylation) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Haloperidol 一般被認為是多巴胺 D2 受體拮抗劑，但本次資料並未提供 MOA，也沒有找到它與岩藻糖基化（fucosylation）路徑的關聯。

**現有資料不支持任何機轉連結。** 這個預測的唯一依據是 TxGNN 知識圖譜分數 0.9991（模型排名第 2416），沒有試驗或文獻佐證。這是模型輸出，不是臨床證據。原適應症與新適應症的相似性分析也尚未完成。

TxGNN 對此藥的其他預測也是同樣情況，全部為 L5、無試驗、無文獻：

| 排名 | 預測適應症 | 預測分數 | 備註 |
|------|-----------|---------|------|
| 2 | 視網膜失養症，伴或不伴眼外異常 (Retinal dystrophy with or without extraocular anomalies) | 99.91% | 可能經由 sigma-1 受體，但只是推測，尚未評估 |
| 3 | 無腦畸形 (Hydranencephaly) | 99.90% | 屬結構性先天腦畸形，缺乏藥理依據 |
| 4 | X 連鎖近視 (Myopia X-linked) | 99.89% | 無佐證 |
| 5 | 夏科-馬利-杜斯氏症，脫髓鞘型 1G (Charcot-Marie-Tooth disease, demyelinating, type 1G) | 99.89% | Haloperidol 已知有錐體外症狀等神經系統副作用，用於神經病變需謹慎（一般藥理提醒，非來自本次資料） |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 18 張許可證，以下列出 5 張主要許可證。資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64839 | HALOPERIDOL-NEURAXPHARM TABLETS 1MG | HIND WING CO LTD |
| HK-54962 | HALOPERIDOL INJ 5MG/ML | AMDIPHARM MERCURY (HONG KONG) LIMITED |
| HK-65060 | HALOPERIDOL-NEURAXPHARM DECANOATE SOLUTION FOR INJECTION 100MG/ML | HIND WING CO LTD |
| HK-65430 | HALOPERIDOL-NEURAXPHARM TABLETS 5MG | HIND WING CO LTD |
| HK-62669 | HALOPERIDOL KERN PHARMA ORAL DROPS 2MG/ML | HIND WING CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有 TxGNN 分數，沒有試驗、文獻，也沒有可成立的機轉連結。
- 香港仿單的警語與禁忌資料缺漏（屬阻斷性缺口），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症（阻斷性缺口）。
- 從 DrugBank 補充作用機轉（MOA）資料。
- 檢索 Haloperidol 與岩藻糖基化異常、或與其他預測疾病的機轉研究和文獻，確認是否有生物學依據。
- 若前述查證找到支持證據，再評估給藥途徑相容性與相似性分析。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

