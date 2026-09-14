---
layout: default
title: Sennosides
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 5
---

# Sennosides
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

Using no skill — this is a direct content-generation task against an explicit template; no coding/debugging/design-decision skill applies here.

# Sennosides：從瀉劑到多項低度可信度候選適應症（建議 Hold）

## 一句話總結

Sennosides 為蒽醌類刺激性瀉劑，經腸道菌叢代謝後刺激大腸蠕動、抑制水分再吸收。
TxGNN 模型列出 **5 個候選新適應症**（禿髮相關疾病 3 項、青光眼 2 項），
但目前**無臨床試驗、無文獻**支持，且機轉分析顯示這些關聯多屬知識圖譜雜訊連結，證據等級均為 **L5**，建議 **Hold**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 便秘（依 sennosides 藥理作用推斷；本地仿單資料缺失） |
| 預測新適應症（Top 1） | Hypotrichosis simplex of the scalp（頭皮單純性稀髮症） |
| TxGNN 預測分數（Top 1） | 99.29% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 全部候選適應症一覽

| 排名 | 疾病 | TxGNN 分數 | 機轉合理性評估 |
|------|------|-----------|----------------|
| 1 | Hypotrichosis simplex of the scalp | 99.29% | 與毛囊生長通路（Wnt/β-catenin、雄性素受體）無已知關聯，推測為代謝節點雜訊連結 |
| 2 | Congenital hypotrichosis milia | 99.23% | 為 LIPH/LPAR6 等基因突變之先天疾病，與腸道瀉下機轉無交集，判斷為偽陽性 |
| 3 | Diffuse alopecia areata | 99.12% | 自體免疫（CD8+ T 細胞）介導疾病，sennosides 無免疫調節作用；長期腹瀉反而可能不利毛髮健康，方向相反 |
| 4 | Open-angle glaucoma | 99.11% | Sennosides 全身吸收極低，無穿透血眼屏障證據，與房水動力學無藥理基礎 |
| 5 | Primary hereditary glaucoma | 99.10% | 與 MYOC/CYP1B1 基因突變相關之遺傳疾病，與腸道局部作用完全無交集 |

## 為什麼這些預測缺乏合理性？

目前缺乏 sennosides 詳細 MOA 官方資料，但依評估報告中的機轉描述：sennosides 屬蒽醌類刺激性瀉劑，經腸道菌叢代謝為活性代謝物 rheinanthrone，作用侷限於大腸黏膜與腸肌間神經叢，藥物全身吸收極低。

5 個候選適應症分屬「禿髮/毛囊發育」與「青光眼」兩大類，其致病機轉（毛囊生長週期調控、自體免疫攻擊、房水排出阻力、特定基因突變）皆與腸道局部刺激性瀉下作用無已知或合理的分子連結。TxGNN 分數雖高（>99%），但排名（rank 11776–14188）顯示這些疾病在全模型排序中並非突出候選，推測分數可能來自知識圖譜中代謝／藥物交互作用節點所產生的間接雜訊連結，而非真實生物學關聯。

## 臨床試驗證據

目前無相關臨床試驗登記（5 個候選適應症皆為 0 筆）。

## 文獻證據

目前無相關文獻（5 個候選適應症皆為 0 筆）。

## 香港上市資訊

Sennosides 目前**未在香港上市**（market_status: 未上市，許可證數: 0），無許可證資料可列出。

## 安全性考量

安全性資訊請參考原廠仿單。目前本地監管機構之仿單警語與禁忌症資料缺失（標記為 Blocking 等級資料缺口），在補齊前無法進行 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個候選適應症證據等級皆為 L5（僅模型預測，無任何臨床試驗或文獻支持）
- 機轉分析一致顯示與原藥理作用無合理連結，多項被評估為知識圖譜偽陽性連結
- 缺乏本地仿單安全性資料（Blocking 等級），無法進入安全性初評

**若要推進需要：**
- 補齊 TFDA/當地藥監局仿單警語與禁忌症資料（解除 Blocking 缺口）
- 查詢 DrugBank API 取得完整 MOA 資料
- 若日後出現體外/體內機轉研究或病例報告，重新評估證據等級
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

