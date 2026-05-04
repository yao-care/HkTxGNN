---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 1
---

# Adapalene
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

# ADAPALENE：從痤瘡治療到血漿鋅升高

## 一句話總結

ADAPALENE 是一種合成類視黃醇（Retinoid），原本以外用製劑用於痤瘡（青春痘）的治療。TxGNN 模型預測它可能對**血漿鋅升高（Zinc, Elevated Plasma）** 有潛在療效，預測分數高達 **99.51%**。然而目前**無任何臨床試驗或文獻**支持此新方向，屬純模型預測結果，需謹慎評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痤瘡（青春痘）／痤瘡桿菌感染性皮膚病（依藥品分類，系統內無核准適應症資料） |
| 預測新適應症 | 血漿鋅升高（Zinc, Elevated Plasma） |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

ADAPALENE（DB00210）屬第三代合成類視黃醇（Synthetic Retinoid），以外用形式作用於皮膚角質細胞，主要透過選擇性結合**視黃酸受體（RAR-β、RAR-γ）**，調節細胞分化與發炎反應，臨床上廣泛用於痤瘡治療。然而本次 Evidence Pack 標記作用機轉（MOA）資料缺失（Data Gap），以下分析以藥物分類知識為基礎。

**機轉上的潛在關聯性**：類視黃醇受體屬於**核受體超家族（Nuclear Receptor Superfamily）**，其轉錄調控活性高度依賴含鋅的「鋅指蛋白結構（Zinc Finger Domain）」。RAR 受體本身即含鋅指結構，當 Adapalene 與 RAR 結合後，可能影響鋅離子的細胞內分布與代謝動態，進而對血漿鋅濃度產生間接的調節效應。此外，維生素 A 代謝路徑中，視黃醇脫氫酶等關鍵酶為鋅依賴性酶，類視黃醇藥物有可能透過這些酶間接影響全身鋅的代謝平衡。

**預測合理性的侷限**：血漿鋅升高（Hyperzincemia）在臨床上相對罕見，多見於鋅補充過量或特定遺傳代謝異常。目前 TxGNN 模型雖給出極高預測分數（99.51%），但完全缺乏臨床或實驗室層級的驗證，預測的生物學機制連結屬推測性質，需要更深入的機轉研究加以確認。

---

## 臨床試驗證據

目前無 ADAPALENE 用於血漿鋅升高的相關臨床試驗登記。

---

## 文獻證據

目前無 ADAPALENE 用於血漿鋅升高的相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本次 Evidence Pack 中，警語、禁忌症及藥物交互作用資料均標記為 Data Gap，建議優先查閱 DrugBank（DB00210）及藥品原廠仿單以取得完整安全性資訊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數雖高（99.51%），但**完全缺乏臨床試驗與文獻支持**，屬 L5 最低證據等級，目前不具備推進再利用研究的科學基礎。
- 「血漿鋅升高」作為適應症在臨床上定義較模糊，且 Adapalene 為外用製劑，若欲影響血漿鋅代謝，需評估其系統性吸收量是否足夠，藥物形式適用性存疑。

**若要推進需要：**
- 補齊 ADAPALENE 完整 MOA 資料（DrugBank API / 原廠仿單）
- 進行體外（in vitro）實驗，驗證 Adapalene 對鋅代謝酶或鋅指蛋白的影響
- 確認「血漿鋅升高」的臨床定義及其疾病負擔，評估是否具備足夠的再利用價值
- 評估外用劑型系統性吸收量（生體可用率），確認是否有足夠血中濃度可影響鋅代謝
- 查閱是否有類視黃醇藥物與鋅代謝相關的基礎研究，作為機轉橋接依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

