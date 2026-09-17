---
layout: default
title: Vonoprazan
parent: 高證據等級 (L1-L2)
nav_order: 800
evidence_level: L2
indication_count: 5
---

# Vonoprazan
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Vonoprazan：從未上市藥物到消化性潰瘍活動期評估

## 一句話總結

Vonoprazan 目前在香港尚未取得藥品許可證，原廠核准適應症與作用機轉等基礎資料均有缺口。
根據 Evidence Pack 中的機轉分析，TxGNN 模型預測其對**消化性潰瘍活動期 (Active Peptic Ulcer Disease)** 有效，
目前有 **2 個臨床試驗**和 **18 篇文獻**支持這個方向，證據等級達到 L2。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港尚無許可證核准資料（原廠適應症未收錄） |
| 預測新適應症 | 消化性潰瘍活動期 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

藥物層級的作用機轉（MOA）欄位本身有資料缺口，但 Evidence Pack 針對此預測適應症提供了具體的機轉推論：Vonoprazan 為**鉀離子競爭性酸阻斷劑（P-CAB）**，可逆性競爭抑制胃壁細胞的 H⁺/K⁺-ATPase，直接且持續地阻斷胃酸分泌。

值得注意的是，此預測本身被標註為「非典型再利用，屬原廠核心適應症延伸」——換言之，消化性潰瘍活動期很可能就是 Vonoprazan 已知或核心的臨床用途之一，而非傳統定義下的全新老藥新用機會。TxGNN 給出接近 100% 的分數，反映的是知識圖譜中「抑酸機轉→潰瘍癒合」這條高度直接的因果連結。

抑制胃酸分泌是消化性潰瘍治療的核心原理，機轉上的合理性極高。也因此，本報告雖名為「老藥新用評估」，實際上更接近對一個機轉明確、證據充分的既有適應症進行資料完整度盤點，而非探索性的新機轉假設。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03214952](https://clinicaltrials.gov/study/NCT03214952) | N/A（上市後監測） | 已完成 | 3183 | Takecab（vonoprazan）於胃潰瘍、十二指腸潰瘍、逆流性食道炎患者的真實世界安全性與有效性大型監測 |
| [NCT03116841](https://clinicaltrials.gov/study/NCT03116841) | Phase 4 | 已完成 | 3 | 探索性評估 vonoprazan 20mg 對逆流性食道炎患者睡眠障礙的影響，樣本量極小，僅間接相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28988197](https://pubmed.ncbi.nlm.nih.gov/28988197/) | 2018 | RCT | Gut | Vonoprazan 於長期 NSAID 治療中預防潰瘍復發，非劣於 lansoprazole，延長使用安全性佳 |
| [28267236](https://pubmed.ncbi.nlm.nih.gov/28267236/) | 2017 | RCT | Dig Endosc | 前瞻性隨機對照試驗顯示 vonoprazan 對內視鏡黏膜下剝離術（ESD）後人工胃潰瘍具療效 |
| [38976448](https://pubmed.ncbi.nlm.nih.gov/38976448/) | 2025 | Phase 3 RCT | Am J Gastroenterol | 同類 P-CAB 藥物 zastaprazan 治療糜爛性食道炎，療效不劣於 esomeprazole，佐證此藥物類別機轉 |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧/網絡統合分析 | Am J Gastroenterol | P-CAB 類藥物於 Grade C/D 重度食道炎療效與安全性不劣於甚至優於 PPI |
| [39156336](https://pubmed.ncbi.nlm.nih.gov/39156336/) | 2024 | 回顧文獻 | Cureus | 全面回顧 vonoprazan 於 GERD、消化性潰瘍、H. pylori 感染等胃酸相關疾病的療效與安全性 |
| [32998241](https://pubmed.ncbi.nlm.nih.gov/32998241/) | 2020 | 回顧文獻 | Pharmaceuticals | 探討 vonoprazan 作為 H. pylori 根除治療的潛在效益 |
| [26369775](https://pubmed.ncbi.nlm.nih.gov/26369775/) | 2016 | PK/PD 回顧 | Clin Pharmacokinet | Vonoprazan（Takecab）藥動藥效特性，涵蓋胃十二指腸潰瘍、逆流性食道炎等核准用法 |
| [22512618](https://pubmed.ncbi.nlm.nih.gov/22512618/) | 2012 | 藥物化學研究 | J Med Chem | TAK-438（vonoprazan 前身）開發過程，證實其 H⁺/K⁺-ATPase 抑制活性強於傳統 PPI |
| [36660052](https://pubmed.ncbi.nlm.nih.gov/36660052/) | 2023 | 回顧文獻 | JGH Open | H. pylori 感染管理指引，涵蓋消化性潰瘍診斷治療建議 |
| [41415806](https://pubmed.ncbi.nlm.nih.gov/41415806/) | 2025 | 回顧文獻 | Front Microbiol | H. pylori 根除治療的最新進展與治療策略 |

---

## 香港上市資訊

目前 Vonoprazan 於香港**尚未取得藥品許可證**（0 張），市場狀態為「未上市」，無核准適應症文字可供比對。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 消化性潰瘍活動期此一預測適應症已有 1 項 Phase 4 大型上市後監測（N=3183）及多篇 RCT/系統性回顧支持，機轉上與抑酸治療潰瘍癒合直接相關，證據等級達 L2。
- 然而，兩項藥物層級資料存在缺口：**TFDA 仿單警語/禁忌**（DG001，Blocking 等級，直接阻擋進入 S1 安全性初評）與**作用機轉 MOA**（DG002，High 等級，影響機轉關聯性正式分析）。在這兩項補齊前，無法完整進入下一決策階段。

**若要推進需要：**
- 下載並解析原廠仿單 PDF，補齊警語與禁忌症資料（DG001，來源：TFDA 官網）— 此為進入 S1 的必要條件
- 透過 DrugBank API 查詢正式 MOA 資料，補強機轉關聯性分析（DG002）
- 追蹤香港藥品許可證申請進度（目前 0 張、未上市）
- 其餘 4 項預測適應症（gastrojejunal ulcer、peptic ulcer perforation、hiatus hernia、achlorhydria）證據等級較低（L3–L5），其中 achlorhydria 完全無臨床試驗或文獻支持，且機轉分析指出其可能反映藥物不良反應方向而非治療適應症，不建議列入近期推進候選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

