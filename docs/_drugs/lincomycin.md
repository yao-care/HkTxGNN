---
layout: default
title: Lincomycin
parent: 僅模型預測 (L5)
nav_order: 523
evidence_level: L5
indication_count: 3
---

# Lincomycin
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

# Lincomycin：從細菌感染到高澱粉酶血症

## 一句話總結

Lincomycin 是林可黴素類（lincosamide）抗生素，用於抗菌治療。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗菌治療（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.14% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏完整的作用機轉資料庫記錄。已知 Lincomycin 是林可黴素類抗生素，透過結合細菌 50S 核糖體次單位來抑制蛋白質合成。

**坦白說，這個預測的機轉合理性很低。** 高澱粉酶血症是一種實驗室檢驗異常，通常反映胰臟或唾液腺受損，並不是獨立、可直接治療的疾病。抗菌藥物作用於細菌核糖體，與澱粉酶升高之間沒有已知的藥理關聯。

這個高分較可能是知識圖譜的關聯假象（association artifact），而不是真正的治療潛力。同一藥物的另外兩個預測也有類似問題：

| 預測適應症 | TxGNN 分數 | 評估 |
|-----------|-----------|------|
| 多株性高黏滯症候群 (Polyclonal hyperviscosity syndrome) | 99.14% | 與第 1 名分數完全相同，疑為圖譜拓撲假象；抗菌藥對免疫球蛋白生成或血漿黏滯度無已知作用 |
| 先天性無白蛋白血症 (Congenital analbuminemia) | 99.06% | 屬 ALB 基因突變的罕見疾病，抗菌機轉無法處理基因層級缺陷；疾病罕見、圖譜鄰域稀疏，可能使分數偏高 |

三個預測都沒有臨床試驗或文獻支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55681 | LINCOMYCIN INJ 300MG/ML | DELTAPHARM LIMITED |
| HK-61712 | LINCOMYCIN SOLUTION FOR INJECTION 300MG/ML (TA FONG) | YAT SENG TRADING CO |
| HK-66152 | LINCOMYCIN SOLUTION FOR INJECTION 3000MG/10ML | KAI YUEN PHARMACEUTICAL LIMITED |
| HK-60253 | LINCO INJ 300MG/ML | ATLANTIC PHARMACEUTICAL LIMITED |
| HK-41155 | TAMCOCIN CAP 500MG | PERFECT GROUPS LTD |

香港共有 7 張許可證，此處列出資料中的 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症都只有模型分數，沒有臨床試驗、文獻或可信的機轉連結（證據等級 L5）。
- 預測的疾病多為實驗室異常或與抗菌機轉無關的遺傳性疾病，較可能是模型假象，不建議投入資源。

**若要推進需要：**
- 取得香港衛生署（Department of Health）仿單，補齊警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 確認高澱粉酶血症等預測是否只是藥品不良反應與疾病的資料關聯，而非治療關係
- 若仍要探索，先做系統性文獻回顧，找出任何支持性的機轉或臨床線索，再重新評估

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

